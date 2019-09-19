from .CMailBackend import MyEmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .CSettings import CSettings
from .CCrypto import CCrypto
import random

class SendMail:
    
    # Email Variables
    subject = 'Subject'
    body = 'Body'
    from_email = ''
    to_email = ''

    def __init__(self, subject, body, from_email, to_email):
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.to_email = to_email

    # Generate message id
    def msgID(self) :
        id = ''
        x = {}
        for i in range(10) :
            x[i] = random.randint(0, 9)
            id = id + str(x[i])

        return 'ID' + id

    # Validator
    def validateData(self) :
        errList = {}

        try :
            validate_email(self.from_email)
        except Exception as e : 
            errList[self.from_email] = e.args
        
        for em in self.to_email :
            try :
                validate_email(em)
            except Exception as e :
                errList[em] = e.args
            
        return errList
    
    # Send email function
    def sendMessage(self):
        message = 'email did not send'

        # validate data
        errList = self.validateData()
        if len(errList) == 0 :
            # get smtp settings
            settings = CSettings()
            smtp = settings.getSettings()
            
            dicSMTP = {}
            for s in smtp:
                if s.val == '' :
                    s.val = None

                if s.val == 'on' :
                    s.val = True

                # decoding password from stringbyte to real password
                if s.name == 'password' :
                    coder = CCrypto()
                    s.val = coder.decode((s.val).encode('utf-8'))

                dicSMTP[s.name] = s.val
            
            # send email
            msgid = self.msgID()
            email = MyEmailMessage(self.subject, self.body, self.from_email, to=self.to_email, headers={'Message-ID': msgid})
            email.setSettings(**dicSMTP)
            #email.setSettings('host', port, 'user@mail.com', 'password', None, None)
            #email.send()
            try :
                email.send()
                message = 'Email sent. Message ID: ' + msgid
            except Exception as e :
                errList['smtpErr'] = e.args
        
        answer = {
            'errList' : errList,
            'message' : message,
        }

        return answer