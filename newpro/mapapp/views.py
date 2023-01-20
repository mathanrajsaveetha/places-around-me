from django.shortcuts import render

def map(request):
    return render(request,'mapapp/map.html')
def admin1(request):    
    return render(request,'mapapp/admin1.html')
def ece(request):    
    return render(request,'mapapp/ece.html')
def eee(request):    
    return render(request,'mapapp/eee.html')
def cse(request):    
    return render(request,'mapapp/cse.html')
def rb(request):    
    return render(request,'mapapp/rb.html')
def girls(request):    
    return render(request,'mapapp/g.html')
def boys(request):    
    return render(request,'mapapp/b.html')
