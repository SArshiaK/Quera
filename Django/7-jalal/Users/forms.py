from django import forms
from .models import CustomUser

def validate_fullname(value):
    if value.find(' ') == -1:
        raise forms.ValidationError('Invalid fullname')
        # print("space problem")

    elif value[0].islower() or value[value.find(' ')+1].islower():
        # print('found problem')
        raise forms.ValidationError('Invalid fullname')
    return True

class CustomUserForm(forms.ModelForm):
    national_code = forms.CharField(min_length=10,max_length=10)
    full_name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class':'input'}), validators=[validate_fullname])


    def clean(self, *args, **kwargs):
        fname = self.cleaned_data.get('full_name')
        if fname == 's':
            raise forms.ValidationError(fname + "'s learn_times is more than 8 hours, please check!")
        return super().clean(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = '__all__'