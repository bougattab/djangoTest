from django.contrib import admin
from api_test import serializers

admin.site.register(serializers.GroupSerializer))
admin.site.register(serializers.UserSerializer)

# Register your models here.
