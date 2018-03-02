from django.shortcuts import render
 
def error_404(request):
        data = {}
        return render(request,'pages/coming_soon.html', data)
 
def error_500(request):
        data = {}
        return render(request,'pages/coming_soon.html', data)