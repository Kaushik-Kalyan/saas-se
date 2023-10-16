from django.shortcuts import render
from django.http import HttpResponse
from falcon import gradio_test


# Create your views here.
def chat(request):
    if request.method=='POST':
        query=request.POST['query']
        res = gradio_test.submit(str(query))
        context={}
        context['output']=res
        print(context)
        return render(request,'falcon/chat.html',context)
    else:
        return render(request,'falcon/chat.html')

