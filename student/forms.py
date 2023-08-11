from student.models import Student, GenderChoices
from django import forms

#   class EmployeeForm(forms.Form):
#       firstname
#       lastname
#       department
#       age
#       gender
#       profession
#       branch

type_choices = (
    (1, "First"),
    (2, "Second")
)


class ContactForm(forms.Form):
    fullname = forms.CharField(
        max_length=125,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text="Inter your fullname"
    )
    phone_number = forms.CharField(max_length=13)
    message = forms.CharField(max_length=500)
    type = forms.ChoiceField(choices=type_choices)
    type = forms.ChoiceField(choices=GenderChoices.choices)

    def clean(self):
        super(ContactForm, self).clean()
        phone_number = self.cleaned_data.get("phone_number")
        if not str(phone_number).startswith("+998"):
            self._errors["phone_number"] = self.error_class(
                ["Invalid phone number! It should start with +998!"]
            )
        return self.cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
