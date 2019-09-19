from ..models import MailSettings
from .CCrypto import CCrypto

class CSettings:

    def setsettings(self, post):
        settings = MailSettings.objects.all()

        for s in settings :
            if post.get(s.name, None) :
                s.val = post[s.name]
            else :
                s.val = ''

            # encoding password to byte and present this byte as string (string.decode('utf-8'))
            if s.name == 'password' :
                coder = CCrypto()
                s.val = coder.encode(s.val).decode('utf-8')
            
            s.save()

    def getSettings(self):
        settings = MailSettings.objects.all()
        return settings