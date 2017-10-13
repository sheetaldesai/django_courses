from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=100)
    desc = forms.CharField(widget=forms.Textarea)


    