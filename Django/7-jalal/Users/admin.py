from Users.models import CustomUser
from django.contrib import admin

#from django_jalali.admin.filters import JDateFieldListFilter
#import django_jalali.admin as jadmin
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    def first_name(self, user):
        fullname = user.full_name.split()
        return fullname[0]

    def last_name(self, user):
        fullname = user.full_name.split()
        return fullname[1]

    list_display = ('username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date')
    search_fields = ['username', 'full_name']
    ordering = ('ceremony_datetime',)
admin.site.register(CustomUser, CustomUserAdmin)



