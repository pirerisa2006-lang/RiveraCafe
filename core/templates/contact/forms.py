from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre *", min_length=3, max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email *",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        label="Mensaje *", min_length=10, max_length=2000,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
    )
