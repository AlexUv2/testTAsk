from django.contrib import admin
from .models import Alias, Target

admin.site.register(Alias)
admin.site.register(Target)
