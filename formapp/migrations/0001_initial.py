# Generated by Django 4.1.5 on 2023-01-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=60, verbose_name='User Name')),
                ('UserEmail', models.EmailField(max_length=60, verbose_name='E-Mail')),
                ('BuildName', models.CharField(choices=[('w-Entry_CSM_GA_Windows', 'Entry_CSM_GA_Windows'), ('w-Entry_CSM_GA_QNX', 'Entry_CSM_GA_QNX'), ('w-Entry_IPC_GA_QNX', 'Entry_IPC_GA_QNX'), ('w-Entry_IPC_GA_Windows', 'Entry_IPC_GA_Windows'), ('w-High_IPC_QNX', 'High_IPC_QNX'), ('w-High_IPC_Windows', 'High_IPC_Windows'), ('w-High_RTOSApp_SingleApp_QNX', 'High_RTOSApp_SingleApp_QNX'), ('w-High_RTOSApp_SingleApp_Windows', 'High_RTOSApp_SingleApp_Windows'), ('w-High_FCC_Windows', 'High_FCC_Windows'), ('w-High_FCC_QNX', 'High_FCC_QNX'), ('w-High_RCC_QNX', 'High_RCC_QNX'), ('w-High_RCC_Windows', 'High_RCC_Windows'), ('w-High_Updater_QNX', 'High_Updater_QNX'), ('w-High_Updater_Windows', 'High_Updater_Windows')], default='w-Entry_CSM_GA_Windows', max_length=39)),
                ('BranchName', models.CharField(max_length=100, verbose_name='User Name')),
                ('CommitID', models.CharField(blank=True, max_length=100, verbose_name='Commit ID')),
                ('DisplaySet', models.CharField(max_length=100, verbose_name='DisplaySet')),
                ('System', models.CharField(choices=[('w-MainLine', 'MainLine'), ('w-PATAC-PHEV', 'PATAC-PHEV'), ('w-R1', 'R1'), ('w-R2', 'R2'), ('w-R2-PATAC', 'R2-PATAC'), ('w-R3', 'R3')], default='w-MainLine', max_length=29)),
                ('BuildMode', models.CharField(choices=[('w-debug', 'Debug'), ('w-release', 'Release')], default='w-debug', max_length=29)),
                ('JiraTicketLink', models.CharField(max_length=200, verbose_name='Jira Ticket Link')),
                ('Comment', models.CharField(max_length=200, verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue name')),
                ('Address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=20, verbose_name='zip code')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Venue Repo')),
                ('web', models.URLField(blank=True, verbose_name='Venue web')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Venue email')),
            ],
        ),
    ]
