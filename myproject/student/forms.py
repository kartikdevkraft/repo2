from django import forms
from student.models import *
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_phone(self):
        # 1. Get the data that has already been cleaned by basic validators
        phone = self.cleaned_data.get('phone')

        # 2. Implement your custom validation logic
        if phone and not str(phone).startswith(('9', '8', '7')):
            # If invalid, raise a ValidationError with the message you want
            raise ValidationError(
                "Phone number must be 10 digits and start with 9, 8, or 7."
            )
        
        # 3. Always return the cleaned data, whether you modified it or not
        return phone