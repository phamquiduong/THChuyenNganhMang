from django.contrib import admin

# Register your models here.
from .models import Account, Contest, Status, RegisterContest, Language

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ContestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class StatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class RegisterContestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class LanguageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(RegisterContest, RegisterContestAdmin)
admin.site.register(Language, LanguageAdmin)