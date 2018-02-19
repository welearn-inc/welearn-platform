from django.shortcuts import render

def google_verify_page(request):
    return render(request, 'misc/google.html',{})