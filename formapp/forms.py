from xml.dom import ValidationErr
from django import forms
from django import forms
from django.forms import ModelForm
  
COUNTRY_CHOICES =( 
    ("1", "Philippines"), 
    ("2", "Japan"), 
    ("3", "Korea"), 
    ("4", "Singapore"), 
    ("5", "USA"), 
)
CHOICES=[('male','Male'),
         ('female','Female')]

Build_Name_list= [
    # ('blank','---------------------------------'),
    ('Entry_CSM_GA_Windows','Entry_CSM_GA_Windows'),
    ('Entry_CSM_GA_QNX','Entry_CSM_GA_QNX'),
    ('Entry_IPC_GA_QNX','Entry_IPC_GA_QNX'),
    ('Entry_IPC_GA_Windows','Entry_IPC_GA_Windows'),
    ('High_IPC_QNX','High_IPC_QNX'),
    ('High_IPC_Windows','High_IPC_Windows'),
    ('High_RTOSApp_SingleApp_QNX','High_RTOSApp_SingleApp_QNX'),
    ('High_RTOSApp_SingleApp_Windows','High_RTOSApp_SingleApp_Windows'),
    ('High_FCC_Windows','High_FCC_Windows'),
    ('High_FCC_QNX','High_FCC_QNX'),
    ('High_RCC_QNX','High_RCC_QNX'),
    ('High_RCC_Windows','High_RCC_Windows'),
    ('High_Updater_QNX','High_Updater_QNX'),
    ('High_Updater_Windows','High_Updater_Windows'),
    ]

System_list= [
    ('MainLine','MainLine'),
    ('PATAC-PHEV','PATAC-PHEV'),
    ('R1','R1'),
    ('R2','R2'),
    ('R2-PATAC','R2-PATAC'),
    ('R3','R3'),
    ]


Build_Mode_list= [
    ('debug', 'Debug'),
    ('release', 'Release'),
    ]

class StudentForm(ModelForm):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  
    country  = forms.ChoiceField(choices = COUNTRY_CHOICES)
    date  = forms.DateField()
    age = forms.DecimalField()
    email = forms.EmailField()
    photo = forms.FileField()
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect) 
    accept  = forms.BooleanField(label="Accept privacy and terms")
  
    def __str__(self):
        return self.firstname
    
# class BuildRequest(forms.Form):

#     UserName = forms.CharField(label='User Name', max_length=60)
#     UserEmail = forms.EmailField(label='E-Mail', max_length=60)
#     BuildName = forms.CharField(label='Select The Build Name', widget=forms.Select(choices=Build_Name_list))
#     BranchName = forms.CharField(label='User Name', max_length=100)
#     CommitID = forms.CharField(label='Commit ID', max_length=100, required=False)
#     DisplaySet = forms.CharField(label='DisplaySet', max_length=100)
#     # BranchName = models.CharField('branchname', max_length=100)
#     System = forms.CharField(label='Select The System', widget=forms.Select(choices=System_list))
#     BuildMode = forms.CharField(label='Select The Build Mode', widget=forms.Select(choices=Build_Mode_list))
#     JiraTicketLink = forms.CharField(label='Jira Ticket Link', max_length=200)
#     Comment = forms.CharField(label='Comment', max_length=200)

#     def __str__(self):
#         return self.UserEmail
    
class BuildRequestForm(forms.Form):

    # UserName = forms.CharField(label='User Name', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter Employee Name', "autocomplete":"off"}))
    UserName = forms.CharField(label='User Name', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter Employee Name'}))
    UserEmail = forms.EmailField(label='E-Mail', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Eg : name.name@rampgroup.com'}))
    BuildName = forms.CharField(label='Select The Build Name', widget=forms.Select(choices=Build_Name_list))
    BranchName = forms.CharField(label='Branch Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Name of Branch'}))
    CommitID = forms.CharField(label='Commit ID', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional*'}))
    DisplaySet = forms.CharField(label='DisplaySet', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter the Displayset ID'}))
    # BranchName = models.CharField('branchname', max_length=100)
    System = forms.CharField(label='Select The System', widget=forms.Select(choices=System_list))
    BuildMode = forms.CharField(label='Select The Build Mode', widget=forms.Select(choices=Build_Mode_list))
    JiraTicketLink = forms.CharField(label='Jira Ticket Link', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter Jira Ticket'}))
    Comment = forms.CharField(label='Comment', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter Text here..'}))

    def __str__(self):
        try:
            return self.UserEmail
        except AttributeError:
            return "No worry"
    
    def clean_dropdown_field(self):
        dropdown_value = self.cleaned_data['Build_Name_list']
        if dropdown_value == 'blank':
            raise ValidationErr("You can't select Empty drop down.")
        """
        Doubts...
        1. how to show error if user select particular element from dropdown in django.

        2. show error and prevent submitting form when user select option 2.

        """
        return dropdown_value