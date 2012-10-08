from os import environ


def sendgridify():
    """
    Return a tuple containing email configuration for the SendGrid Heroku
    add-on by analyzing the environment variables

    Will raise an EnvironmentError if the add-on does not appear to be
    installed.

    Example usage:

    from sendgridify import sendgridify
    EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, \
    EMAIL_USE_TLS = sendgridify()
    """

    host = 'smtp.sendgrid.net'
    host_user = environ.get('SENDGRID_USERNAME', None)
    host_password = environ.get('SENDGRID_PASSWORD', None)
    port = 587
    use_tls = True

    if not host_user or not host_password:
        raise EnvironmentError('Please install the Heroku SendGrid add-on')

    return (
        host,
        host_user,
        host_password,
        port,
        use_tls,
    )
