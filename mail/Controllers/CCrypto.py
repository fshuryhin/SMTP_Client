from base64 import urlsafe_b64encode, urlsafe_b64decode

class CCrypto:
    key = '12345678'
    
    # Function encode string intu byte
    # byte can be represented as bytestring with: byte.decode('utf-8')
    def encode(self, data):
        return urlsafe_b64encode(bytes(self.key+data, 'utf-8'))

    # Function decode byte intu original string
    # enc - this is a byte
    # for stringbyte need string.encode('utf-8') first
    def decode(self, enc):
        return urlsafe_b64decode(enc)[len(self.key):].decode('utf-8')

    def getKey(self):
        return self.key