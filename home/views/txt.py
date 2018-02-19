from django.shortcuts import render

def robots_txt_page(request):
    return render(request, 'misc/robots.txt', {}, content_type="text/plain")

def humans_txt_page(request):
    return render(request, 'misc/credits.txt', {}, content_type="text/plain")