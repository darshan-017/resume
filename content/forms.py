from django import forms
from django.contrib.auth.models import User
from .models import Profile, Education, Experience, Skills


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'email', 'phone', 'image', 'linkedin', 'Git_Hub', 'city', 'state', 'about']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'college', 'percentage', 'university', 'city', 'state']

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job', 'company', 'project', 'about', 'city', 'state',]

class AddSkills(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill', 'rating']
