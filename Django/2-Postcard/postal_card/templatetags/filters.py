# Put you code here
from django import template
persian_numbers = u'۱۲۳۴۵۶۷۸۹۰'

register = template.Library()

def changer(value):
    
    value = value.replace('0', persian_numbers[9])
    value = value.replace('1', persian_numbers[0])
    value = value.replace('2', persian_numbers[1])
    value = value.replace('3', persian_numbers[2])
    value = value.replace('4', persian_numbers[3])
    value = value.replace('5', persian_numbers[4])
    value = value.replace('6', persian_numbers[5])
    value = value.replace('7', persian_numbers[6])
    value = value.replace('8', persian_numbers[7])
    value = value.replace('9', persian_numbers[8])
    return value
register.filter('changer', changer)