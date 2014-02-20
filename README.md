# django-heroku-sendgridify

Automatic email configuration for the Django/Heroku/SendGrid stack

## Install

`pip install django-heroku-sendgridify`

## Usage

In your Django settings module:

    from sendgridify import sendgridify
    EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS = sendgridify()

That's it. Best README ever.
