from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextPassword(BasePasswordHasher):
    algorithm = "plain"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        return "%s$%s$%s" % (self.algorithm, salt, password)

    def verify(self, password, encoded):
        return "plain$$" + password == encoded

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('hash'), encoded),
        ])