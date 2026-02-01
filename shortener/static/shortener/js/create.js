(function(){
      const original = document.getElementById("id_original_url");
      const alias = document.getElementById("id_custom_alias");
      const exp = document.getElementById("id_expires_at");

      if (original) original.placeholder = "https://example.com/very/long/url";
      if (alias) alias.placeholder = "optional-custom-alias";
      if (exp) {
        // If your form field is a DateTimeField, Django may render it as text.
        // This makes it a datetime-local picker in modern browsers.
        exp.type = "datetime-local";
      }
    })();