from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm

def home(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaints')
    else:
        form = ComplaintForm()
    return render(request, 'home.html', {'form': form})

def complaints(request):
    all_complaints = Complaint.objects.all()
    return render(request, 'complaints.html', {'complaints': all_complaints})
