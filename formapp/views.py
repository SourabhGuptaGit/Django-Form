from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django import forms
from .forms import StudentForm, BuildRequestForm
from .models import BuildRequestModel
from .Excel_agent import BuildRequestExcel
from .Mail_agent import Make_table

# Create your views here.
def home(request):
    # return HttpResponse("home page...")
    return render(request, '404.html', {})

from django.views.decorators.cache import cache_control



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def BRform(request):  
    submitted = False
    if request.method == 'POST':
        form = BuildRequestForm(request.POST)
        # form = BuildRequestModel(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            UserName = form.cleaned_data['UserName']
            UserEmail = form.cleaned_data['UserEmail']
            BuildName = form.cleaned_data['BuildName']
            BranchName = form.cleaned_data['BranchName']
            CommitID = form.cleaned_data['CommitID']
            DisplaySet = form.cleaned_data['DisplaySet']
            System = form.cleaned_data['System']
            BuildMode = form.cleaned_data['BuildMode']
            JiraTicketLink = form.cleaned_data['JiraTicketLink']
            Comment = form.cleaned_data['Comment']

            # list_form_data = [UserName,UserEmail,BuildName,BranchName,CommitID,DisplaySet,System,BuildMode,JiraTicketLink,Comment]
            Dict_form_data = {
                'User Name' : UserName,
                'User Email' : UserEmail,
                'Build Name' : BuildName,
                'Branch Name' : BranchName,
                'Commit ID' : CommitID,
                'DisplaySet' : DisplaySet,
                'System' : System,
                'Build Mode' : BuildMode,
                'Jira Ticket Link' : JiraTicketLink,
                'Comment' : Comment
            }
            print(f"\n\n\n{Dict_form_data}\n\n\n")
            print("Mail function trigger kiya hai")
            Make_table(Dict_form_data)
            try:
                BuildRequestExcel([Dict_form_data])
            except PermissionError:
                print("Excel Persssion Error!!!!")
                return render(request, 'somthingwentwrong/sww.html')
            # form.clean()
            
            return HttpResponseRedirect('/brform?submitted=True')
    
    else:
        form = BuildRequestForm
        if 'submitted' in request.GET:
            submitted =True

    return render(request, 'forms.html', {
    # return render(request, 'BR form test.html', {
        'form' : form,
        'Rsubmitted' : submitted
    })

