from django.db import models

# Create your models here.
Build_Name_list= [
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

class BuildRequestModel(models.Model):

    UserName = models.CharField('User Name', max_length=60)
    UserEmail = models.EmailField('E-Mail', max_length=60)
    BuildName = models.CharField(max_length=39, choices=Build_Name_list, default="w-Entry_CSM_GA_Windows")
    BranchName = models.CharField('User Name', max_length=100)
    CommitID = models.CharField('Commit ID', max_length=100, blank= True)
    DisplaySet = models.CharField('DisplaySet', max_length=100)
    # BranchName = models.CharField('branchname', max_length=100)
    System = models.CharField(max_length=29, choices=System_list, default="w-MainLine")
    BuildMode = models.CharField(max_length=29, choices=Build_Mode_list, default="w-debug")
    JiraTicketLink = models.CharField('Jira Ticket Link', max_length=200)
    Comment = models.CharField('Comment', max_length=200)

    def __str__(self):
        return self.UserEmail

