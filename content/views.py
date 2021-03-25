import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Experience, Education, Skills
from .forms import ProfileForm, EducationForm, SignInForm, AddExperienceForm, AddSkills
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def SignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'form': form, 'msg': 'User not found'})
        else:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
        education = Education.objects.filter(user=request.user).all()
        skills = Skills.objects.filter(user=request.user).all()
        profile = Profile.objects.filter(user=request.user).all()
        experience = Experience.objects.filter(user=request.user).all()
        return render(request, 'index.html', {'edu': education, 'skill': skills, 'pro': profile, 'exp': experience})
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
    form = UserCreationForm
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/login')
def personal_detail(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        img = request.FILES['image']
        link = request.POST['linkedin']
        git = request.POST['Git_Hub']
        city = request.POST['city']
        state = request.POST['state']
        about = request.POST['about']
        pro = Profile(fullname=fullname, email=email, phone=phone, image=img, linkedin=link, Git_Hub=git,
                                    city=city,
                                    state=state, about=about, user=request.user)
        pro.save()
        return redirect('index')
    form = ProfileForm()
    return render(request, 'personal_detail.html', {'form': form})

def edit_personal(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid:
            form.save()
            print('Form valid success')
            return redirect('index')
    form = ProfileForm(instance=request.user.profile)
    return render(request, 'personal_detail.html', {'form': form})

@login_required(login_url='/login')
def addEducation(request):
    if request.method == 'POST':
        degree = request.POST['degree']
        college = request.POST['college']
        percentage = request.POST['percentage']
        university = request.POST['university']
        city = request.POST['city']
        state = request.POST['state']
        edu = Education(degree=degree, college=college, percentage=percentage, university=university, city=city, state=state, user=request.user)
        edu.save()
        return redirect('index')
    form = EducationForm()
    return render(request, 'addEducational.html', {'form': form} )

def edit_edu(request, pk):
    edu = Education.objects.get(id=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=edu)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EducationForm(instance=edu)
    return render(request, 'addEducational.html', {'form': form})

@login_required(login_url='/login')
def addExperience(request):
    if request.method == 'POST':
        job = request.POST['job']
        company = request.POST['company']
        project = request.POST['project']
        about = request.POST['about']
        city = request.POST['city']
        state = request.POST['state']
        exp = Experience(job=job, company=company, project=project, about=about, city=city, state=state, user=request.user)
        exp.save()
        return redirect('index')
    form = AddExperienceForm()
    return render(request, 'addExp.html', {'form': form})

def editExp(request, pk):
    exp = Experience.objects.get(id=pk)
    if request.method == 'POST':
        form = AddExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = AddExperienceForm(instance=exp)
    return render(request, 'addExp.html', {'form': form})

@login_required(login_url='/login')
def addSkill(request):
    if request.method == 'POST':
        skill = request.POST['skill']
        rating = request.POST['rating']
        sk = Skills(skill=skill, rating=rating, user=request.user)
        sk.save()
        return redirect('index')
    form = AddSkills()
    return render(request, 'addSkill.html', {'form': form})

def editSkill(request, pk):
    sk = Skills.objects.get(id=pk)
    if request.method == 'POST':
        form = AddSkills(request.POST, instance=sk)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = AddSkills(instance=sk)
    return render(request, 'addSkill.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('index')

def selectResume(request):
    return render(request, 'selectResume.html')

def resume2(request):
    context = {
        'edu': Education.objects.filter(user=request.user).all(),
        'sk': Skills.objects.filter(user=request.user).all(),
        'pro': Profile.objects.filter(user=request.user).all(),
        'exp': Experience.objects.filter(user=request.user).all()
    }
    return render(request, 'type1.html', context)

def weather(request):

    if request.method == 'POST':
        city = request.POST['city']
        country = request.POST['country']
        city = city.lower().capitalize()
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7b391b333ee96bfcf109dbfd46953070&units=metric'.format(city)
            res = requests.get(url)
            data = res.json()
            temp = data['main']['temp']
        except:
            temp = 'Some Server error'

        country_l = country
        country = country.lower()[:2]
        return render(request, 'weather.html', {'temp': temp, 'country': country, 'country_l': country_l})
    return render(request, 'weather.html', {})
