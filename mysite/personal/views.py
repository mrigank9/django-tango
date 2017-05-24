from django.shortcuts import render

#render is actually main, not HttpResponse

def index(request):
    return render(request, 'personal/home.html') #location of html template to be rendered i.e. 'personal.home.hmtl'

#also render looks in a template directory

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to cantact me, please email me','mp09patel@gmail.com']})




#content iskey of dictionary
#also {} is dictionary parameter of render
#i.e. renders html on request with {}
