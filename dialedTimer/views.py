from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . import forms as timer_forms
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


@login_required
def home(request):
    return render(request, 'dialedTimer/home.html')


@login_required
def coffeeForm(request):
    if request.method == 'POST':
        form = timer_forms.CoffeeCreationForm(request.POST)
        if form.is_valid():
            form.save()#the save method of usercreation form automagically saves our user accounts
            coffee_name = form.cleaned_data.get('coffee_name')
            messages.success(request, f'Coffee {coffee_name} was created!')

            return redirect('home')
    else:
        form = timer_forms.CoffeeCreationForm()
    return render(request, 'dialedTimer/coffeeForm.html', {'form': form})


@login_required
def extractionForm(request):
    if request.method == 'POST':
        form = timer_forms.ExtractionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user_id = request.user
            obj.save()#the save method of usercreation form automagically saves our user accounts
            messages.success(request, 'Your extraction was added!')

            return redirect('home')
    else:
        form = timer_forms.ExtractionForm()
    return render(request, 'dialedTimer/extractionForm.html', {'form': form})
def sendMail(request):
    send_mail(
        'Test_Email',
        'Test_Message',
        'contact@brandonmartinez.dev',
        ['contact@brandonmartinez.dev'],
        fail_silently=False,
    )
    return HttpResponse('Mail view executed')
