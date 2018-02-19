from django.shortcuts import render

def terms_page(request):
    return render(request, 'pages/terms.html',{
        'tab': 'terms',
    })
