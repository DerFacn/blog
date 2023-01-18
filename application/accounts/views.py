from django.shortcuts import render
from .forms import SignUpForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form":form})