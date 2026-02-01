from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import ShortURL
from .forms import ShortURLCreateForm, ShortURLEditForm
from django.db.models import Sum
import qrcode
from io import BytesIO
from django.http import HttpResponse

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(owner=request.user).order_by("-created_at")

    total_clicks = urls.aggregate(total=Sum("clicks"))["total"] or 0

    return render(request, "shortener/dashboard.html", {
        "urls": urls,
        "total_clicks": total_clicks,
    })

@login_required
def create_short_url(request):
    if request.method == "POST":
        form = ShortURLCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user

            if obj.custom_alias:
                obj.code = obj.custom_alias
            obj.save()
            return redirect("dashboard")
    else:
        form = ShortURLCreateForm()
    return render(request, "shortener/create.html", {"form": form})

@login_required
def edit_short_url(request, pk):
    obj = get_object_or_404(ShortURL, pk=pk, owner=request.user)
    if request.method == "POST":
        form = ShortURLEditForm(request.POST, instance=obj)
        if form.is_valid():
            updated = form.save(commit=False)
            # keep code synced if alias provided
            if updated.custom_alias:
                updated.code = updated.custom_alias
            updated.save()
            return redirect("dashboard")
    else:
        form = ShortURLEditForm(instance=obj)
    return render(request, "shortener/edit.html", {"form": form, "obj": obj})

@login_required
def delete_short_url(request, pk):
    obj = get_object_or_404(ShortURL, pk=pk, owner=request.user)
    if request.method == "POST":
        obj.delete()
        return redirect("dashboard")
    return render(request, "shortener/delete.html", {"obj": obj})

def redirect_short_url(request, code: str):
    url_obj = get_object_or_404(ShortURL, code=code)

    if url_obj.is_expired():
        raise Http404("This link has expired.")

    # analytics
    url_obj.clicks += 1
    url_obj.save(update_fields=["clicks"])

    return redirect(url_obj.original_url)

# using this anyonw can view the QR code
def public_qr_code_png(request, code: str):
    obj = get_object_or_404(ShortURL, code=code)

    short_url = request.build_absolute_uri(f'/{obj.code}/')

    img = qrcode.make(short_url)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")


# Only authenticated user can view this generated QR code
@login_required
def auth_qr_code_png(request, code: str):
    obj = get_object_or_404(ShortURL, code=code)

    if obj.owner != request.user:
        raise Http404("Not found")

    short_url = request.build_absolute_uri(f'/{obj.code}/')
    img = qrcode.make(short_url)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")

