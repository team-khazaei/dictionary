from django import forms


class TranslateForm(forms.Form):
    STATUS_CHOICES = [
        ("فارسی به انگلیسی", "فارسی به انگلیسی"),
        ("انگلیسی به فارسی", "انگلیسی به فارسی"),
    ]

    language = forms.ChoiceField(widget=forms.Select, choices=STATUS_CHOICES)
    search = forms.CharField(max_length=2000)
