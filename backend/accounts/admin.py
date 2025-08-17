from django.contrib import admin
from .models import UserAccount,LineWorker,SectionOffice,Public

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(LineWorker)
admin.site.register(SectionOffice)
admin.site.register(Public)