from django.shortcuts import render

def privacy_page(request):
    return render(request, 'pages/privacy.html',{
        'tab': 'privacy',
    })
