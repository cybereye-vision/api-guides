from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from  .models import Question,authen_user
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
    myName = "Trieu Hong Ngoc"
    favorite = ["Hat","Xem Phim","An","Taylor Swift"]

    return render(request,"polls/index.html", {"name": myName, "favorite": favorite })

def ham1(request):
    return HttpResponse("<h1>Ham Linh Tinh</h1><p>Xin Chao</p>")

def regiter(request):
    user = request.POST["username"]
    passw = request.POST["password"]
    my_user = authenticate(username=user,password = passw)
    if my_user is None:
        return HttpResponse("<h3>Khong co du lieu nay! </h3>")
    else:
        return render(request,"polls/login.html")



def list_question(request):
    list_question = Question.objects.all()
    #list_question = get_object_or_404(Question,pk=1)
    context = {"listques" : list_question}
    return render(request, "polls/question_list.html",context)


def detailChoice (request,quest_id):
    q = Question.objects.get(pk = quest_id)
    return render(request,'polls/Choice.html',{"qs":q})

def vote (request,quest_id):
    q = Question.objects.get(pk = quest_id)
    dt = request.POST["choice"]
    return HttpResponse(dt)