from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def signup(request):
    return render(request, 'users/signup.html')


@login_required(login_url='/login/')
def index(request):
    """
    from django.http import HttpResponse
    from django.template import loader

    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render())

    template = loader.get_template('mysite/home.html')
    context = {}
    return HttpResponse(template.render(context, request))
    """
    return render(request, 'pages/index.html')

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'users/profile.html')

@login_required(login_url='/login/')
def calendar(request):
    return render(request, 'pages/calendar.html')

@login_required(login_url='/login/')
def statistics(request):
    return render(request, 'pages/stats.html')

@login_required(login_url='/login/')
def tables(request):
    return render(request, 'pages/tables.html')

@login_required(login_url='/login/')
def buttons(request):
    return render(request, 'pages/buttons.html')

@login_required(login_url='/login/')
def editors(request):
    return render(request, 'pages/editors.html')

@login_required(login_url='/login/')
def forms(request):
    return render(request, 'pages/forms.html')
