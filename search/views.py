from requests.exceptions import ConnectionError
from deep_translator import GoogleTranslator

from django.shortcuts import render
from django.views import View

from .forms import TranslateForm


class Translate(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        try:
            form = TranslateForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data.get("search")
                language = form.cleaned_data.get("language")
                count_len = len(text)
                if language == "فارسی به انگلیسی":
                    translated = GoogleTranslator(
                        source="fa", target="en").translate(
                        text=text, return_all=True
                    )
                    dir = "ltr"
                else:
                    translated = GoogleTranslator(
                        source="en", target="fa").translate(
                        text=text, return_all=True
                    )
                    dir = "rtl"
                context = {
                    "method": "POST",
                    "translated": translated,
                    "count_len": count_len,
                    "dir": dir,
                    "text": text,
                }
                return render(request, "index.html", context=context)
            context = {"error": "error"}
            return render(request, "index.html", context=context)
        except ConnectionError:
            context = {"connection": "ارتباط قطع است!"}
            return render(request, "index.html", context=context)   