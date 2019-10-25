from django.shortcuts import render,redirect
from app01.models import *
from datetime import datetime

# Create your views here.

def onlineQA(request):
    questions_list=Questions.objects.all()
    return render(request,"onlineQA.html",{"questions_list":questions_list})

def question(request):
    if request.method=='GET':
        return render(request, "question.html")
    if request.method=='POST':
        title=request.POST.get('title')
        detailDesc=request.POST.get('detailDesc')
        # lastModified=datetime.now()
        Questions.objects.create(title=title,detailDesc=detailDesc,lastModified=datetime.now(),answerCount=0)
        return redirect("/onlineQA/")

def detail(request,id):
    # print(id)
    detail_obj = Questions.objects.filter(id=id).first()
    answers_obj = Answers.objects.filter(questions=id).all()
    if request.method=='GET':
        return render(request,"detail.html",{"detail_obj":detail_obj,"answers_obj":answers_obj})
    if request.method=='POST':
        ansContent=request.POST.get('ansContent')
        Answers.objects.create(ansContent=ansContent,ansDate=datetime.now(),questions_id=id)
        detail_obj.answerCount+=1
        detail_obj.save()
        return render(request,"detail.html",{"detail_obj":detail_obj,"answers_obj":answers_obj})
