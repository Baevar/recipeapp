from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from myauth.models import Profile
from django.contrib.auth.decorators import login_required
from myauth.forms import ProfileForm

def login_view(request:HttpRequest) -> HttpResponse:
    if request.method == "GET":        
        if request.user.is_authenticated:   
            return redirect(reverse("myauth:edit_profile"))
        return render(request, "myauth/login.html")
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password) 
    if user is not None:
        login(request, user)
        return redirect('/recipe')
    return render(request, "myauth/login.html", {"error":"Invalid login credentials"})


class LogoutView(View):
    def get(self, request:HttpRequest) -> HttpResponse:
        logout(request)
        return redirect(reverse("recipeapp:recipe_index"))

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:edit_profile")
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")   
        password = form.cleaned_data.get("password1")
        form.instance.bio = username
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        user = authenticate(                    
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)        
        return response
    
    
@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)

        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if 'save_profile' in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                return redirect('myauth:edit_profile')  

        elif 'change_password' in request.POST:
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user) 
                return redirect('myauth:edit_profile')  
    else:
        profile_form = ProfileForm(instance=profile)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'myauth/edit_profile.html', {
        'profile_form': profile_form,
        'password_form': password_form
    })

