
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import ContactMessage
import logging

logger = logging.getLogger(__name__)


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
            # Save the contact message
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            try:
                # Send email notification
                sent = send_mail(
                    subject=f"Portfolio contact: {subject}",
                    message=(
                        f"Name: {name}\n"
                        f"Email: {email}\n"
                        f"Subject: {subject}\n"
                        f"Message:\n{message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )

                if sent == 1:
                    messages.success(
                        request,
                        "Your message was sent successfully!"
                    )
                else:
                    messages.error(
                        request,
                        "Your message was saved, but email sending failed."
                    )

            except Exception:
                logger.exception("Contact email failed")
                messages.error(
                    request,
                    "Your message was saved, but email sending failed."
                )

        else:
            messages.error(request, "Please fill in all fields.")

        return redirect("home")

    return redirect("home")
