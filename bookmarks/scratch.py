from django.core.mail import send_mail

send_mail(
    "Django mail",
    "This mail was sent with Django",
    "robertcurtiss64@gmail.com",
    ["robertcurtiss64@gmail.com"],
    fail_silently=False,
    auth_user="robertcurtiss64@gmail.com",
    auth_password="upyt mxzb gtzr eure",
)
