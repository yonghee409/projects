from django.shortcuts import render
from .models import *
from .forms import Form_ApiKeyset
#from .models import User

# Create your views here.
def index(request):
    return render(request, 'cc_pf/index.html',{})

def add_apikey(request):
    if request.method=='POST':
        form = Form_ApiKeyset(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Form_ApiKeyset()

    return render(request, 'cc_pf/add_apikey.html',{'form':form})
