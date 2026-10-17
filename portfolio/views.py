from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

# Create your views here.


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message was sent successfully!")
        else:
            messages.error(request, "Please fill in all fields.")

        return redirect("home")

    return redirect("home")
