from django.contrib.auth.hashers import make_password

class PasswordHasher(object):
    def hash_password(self, password):
        return make_password(password)
