from django.shortcuts import render

def projects(request):
    msg = "hello world"
    context = {
        "msg": msg
    }
    return render(request, 'projects/index.html', context=context)
