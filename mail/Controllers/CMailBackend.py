from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

class MyEmailMessage(EmailMessage):
    # SMTP variables
    host = ''
    port = 25
    username = ''
    password = ''
    use_tls = None
    use_ssl = None
    fail_silently = None

    # Set SMTP settings
    def setSettings(self, host, port, username, password, use_tls, use_ssl):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.use_ssl = use_ssl
    
    # Return SMTP EmailBackend settings
    def get_connection(self, fail_silently=False):
        return EmailBackend(self.host, self.port, self.username, self.password, self.use_tls, self.fail_silently, self.use_ssl)