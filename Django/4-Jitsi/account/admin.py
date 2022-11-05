from django.contrib import admin
from .models import Account, Team

class AccountInline(admin.TabularInline):
    model = Account
    extra = 0

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'jitsi_url_path')
    search_fields = ['name']
    inlines = [AccountInline]

class AccountAdmin(admin.ModelAdmin):
    list_display = ('team',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Account, AccountAdmin)
# Register your models here.
