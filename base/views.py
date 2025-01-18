from django.shortcuts import render



rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':1, 'name':'Design with Marv!'},
    {'id':1, 'name':'Frontend Guys!'},
]

def home(request):
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')
