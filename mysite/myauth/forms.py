from myauth.models import Profile
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    first_name = forms.CharField(max_length=150, required=False, label="Имя")
    last_name = forms.CharField(max_length=150, required=False, label="Фамилия")
    email = forms.EmailField(required=False, label="Email")
    
    class Meta:
        model = Profile
        fields = ["bio"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user  # Получаем связанного пользователя
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            profile.save()
            user.save()
            self.save_m2m()  
        return profile