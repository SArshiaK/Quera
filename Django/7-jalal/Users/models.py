from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from freezegun import freeze_time

Gender_CHOICES =(
    ("M", "Male"),
    ("F", "Female")
)

class CustomUser(models.Model):
    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(choices=Gender_CHOICES, max_length=1)
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField()
    ceremony_datetime = jmodels.jDateTimeField()
    country = models.CharField(default='Iran', max_length=4)

    # def first_name(self):
    #     fullname = self.full_name
    #     splited = fullname.split()
    #     return splited[0]
    # def last_name(self):
    #     fullname = self.full_name
    #     splited = fullname.split()
    #     return splited[1]

    def get_first_and_last_name(self):
        fullname = self.full_name
        splited = fullname.split()
        # first_name = splited[0]
        # last_name = splited[1]
        dic = {
           'first_name': splited[0],
            'last_name': splited[1]
        }
        return dic
    # @freeze_time("2022-11-19")
    def get_age(self):
        # I should consider months and maybe dates too.
        
        birthday = self.birthday_date
        current_datetime = jdatetime.datetime.now() 
        year = current_datetime.year - birthday.year
        month = current_datetime.month - birthday.month
        day = current_datetime.day - birthday.day
        if day < 0:
            month -= 1
        if month < 0:
            year -= 1
        # age = (current_datetime.year-birthday.year)
        if year < 0:
            return 0
        return year
    
    def is_birthday(self):
        current = jdatetime.datetime.now()
        
        if self.birthday_date.month == current.month and self.birthday_date.day == current.day:
            return True
        return False




