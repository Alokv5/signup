from django.contrib import admin
from restapi.models import Employee
from django.contrib.auth.models import User, Group

admin.site.register(Employee)
admin.site.unregister(Group)
admin.site.unregister(User)
