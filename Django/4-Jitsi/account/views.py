from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Team, Account, User 
from .forms import SignUpForm, LoginForm, TeamForm

def home(request):    
    if request.method == 'GET':
        user_id = request.user.id
        account = Account.objects.filter(pk = user_id)
        if account[0].team != None:
            team_name = account[0].team.name
            return render(request, 'home.html', {'team': team_name})
        else:
            return render(request, 'home.html', {'team': None})
    return redirect('/')

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, "signup.html", {"form": form})
    if request.method == "POST":
        if form.is_valid():
            signup = form.save(commit=False)
            signup.user = request.user
            signup.save()
            return redirect("/account/team")
        else:
            return render(request, 'signup.html', {'form': form})
    form = SignUpForm()
    return render(request, "signup.html", {"form": form})

def login_account(request):
    form = LoginForm(request.POST or None)
    if request.method == 'GET':
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                return redirect('/account/login/')
        return redirect('/account/login/')
    
def logout_account(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/account/login/')


@login_required(login_url='/accounts/login/')
def joinoradd_team(request):
    if request.method == 'GET':
        user_id = request.user.id
        account = Account.objects.filter(pk = user_id)
        if account[0].id == user_id:
            if account[0].team != None:
                return redirect('/home/')
            else:
                form = TeamForm()
                return render(request, 'team.html', {'fomr': form})
    elif request.method == 'POST':
        form = TeamForm(request.POST or None)
        team_name = request.POST['name']
        if form.is_valid():
            teams = Team.objects.all()
            user = request.user
            user_id = user.id
            account = Account.objects.filter(pk=user_id)
            for i in range(len(teams)):
                if teams[i].name == team_name:
                    account[0].team = teams[i]
                    account[0].save()
                    return redirect('/home/')
            newTeam = Team()
            newTeam.name = team_name
            newTeam.jitsi_url_path = 'http://meet.jit.si/' + team_name
            newTeam.save()
            # return render(request, 'home.html', {'team': })
            account[0].team = newTeam
            account[0].save()
            return redirect('/home/')
        return redirect('/home/')

def exit_team(request):
    if request.method == 'GET':
        current_user = request.user
        accounts = Account.objects.all()
        for i in range(0, len(accounts)):
            if accounts[i].id == current_user.id:
                accounts[i].team = None
                accounts[i].save()
        return redirect('/home/')

