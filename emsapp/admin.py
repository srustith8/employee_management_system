from django.contrib import admin
from .models import Asset,AssignedAsset,Leave
class TopicAdmin(admin.ModelAdmin):
    pass


admin.site.register(Asset)
admin.site.register(AssignedAsset)
admin.site.register(Leave)
