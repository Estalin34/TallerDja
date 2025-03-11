from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    type = forms.JSONField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 2}))

    class Meta:
        model = Pokemon
        fields = ["title", "description", "type", "hp", "attack", "defense", "special_attack", "special_defense", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "hp": forms.NumberInput(attrs={"class": "form-control"}),
            "attack": forms.NumberInput(attrs={"class": "form-control"}),
            "defense": forms.NumberInput(attrs={"class": "form-control"}),
            "special_attack": forms.NumberInput(attrs={"class": "form-control"}),
            "special_defense": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.URLInput(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("No se permiten productos con CFE")
        return title

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image.startswith("https://"):
            raise forms.ValidationError("La imagen debe ser una URL válida")
        return image

    def clean(self):
        cleaned_data = super().clean()
        hp = cleaned_data.get("hp")
        attack = cleaned_data.get("attack")
        defense = cleaned_data.get("defense")
        special_attack = cleaned_data.get("special_attack")
        special_defense = cleaned_data.get("special_defense")

        if hp < 0 or attack < 0 or defense < 0 or special_attack < 0 or special_defense < 0:
            raise forms.ValidationError("Los stats no pueden ser negativos")
        return cleaned_data
