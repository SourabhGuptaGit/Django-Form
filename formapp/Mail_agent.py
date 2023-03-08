import time
import win32com.client as win32
from pretty_html_table import build_table
# from main import event
import pandas as pd
from prettytable import PrettyTable
import pythoncom
from datetime import date, timedelta

cc_list = ['deepscreen.automation@rampgroup.com; Sharath.golla@rampgroup.com; devops@rampgroup.com']
# CC_tags = ['surendra.kalahasti@rampgroup.com; shiva.teegala@rampgroup.com; srikanth.yakasiri@rampgroup.com; pms-v8@rampgroup.com; devops@rampgroup.com']

def event():

    Date = date.today()
    CurrentDate = date.strftime(Date, "%d-%b-%Y")
    t = time.localtime()
    x = int(time.strftime("%H", t))

    if (x > 0) and (x <= 12):
        Event = 'Morning'
        return Event
    elif (x > 12) and (x < 18):
        Event = 'Afternoon'
        return Event
    else:
        Event = 'Evening'
        return Event

def Mail(data : dict, table : list):

    print("Mail function ke andar hai")
    outlook = win32.Dispatch('outlook.application',pythoncom.CoInitialize())
    mail = outlook.CreateItem(0)
    mail.To = data['User Email'] #c.Receiver # ";".join(c.Receiver)
    # mail.CC = ";".join(cc_list)
    mail.Subject = f"DeepScreen Build Request: {data['Build Name']} Branch {data['Branch Name']}"

    mail.HTMLBody = f"""
                    <html><body><p>Hi,</p>
                    <p> </p>
                    <p>Got new build Request from {data['User Email']}</p>
                    <p> </p>
                    {table[0]}
                    
                    
                    <p> </p>
                    <p> </p>
                    <p>From,</p>
                    <p>DevOps Team</p>
                    <p>............</p>
                    </body></html>
                    """

    # mail.HTMLBody = f"""
    #                 <html><body><p>Hi,</p>
    #                 <p> </p>
    #                 <p>Got new build Request from {data['User Email']}</p>
    #                 <p><b>Build Name :</b> {data['Build Name']}</p>
    #                 <p><b>Branch Name :</b> {data['Branch Name']}</p>
    #                 <p><b>SHA :</b> {data['Commit ID']}</p>
    #                 <p><b>DisplaySet :</b> {data['DisplaySet']}</p>
    #                 <p><b>Build Mode :</b> {data['Build Mode']}</p>
    #                 <p><b>Selected System :</b> {data['System']}</p>
    #                 <p><b>Regarding :</b> {data['Comment']}</p>
                    
    #                 <p> </p>
    #                 <p> </p>
    #                 <p>From,</p>
    #                 <p>DevOps Team</p>
    #                 <p>............</p>
    #                 </body></html>
    #                 """


    print(f"\n\n Mail with Data has Sent to  {data['User Email']} on {date.today()}!!\n\n\n")
    mail.Send()

# def table_agent_mail(data):
#     table = PrettyTable()
#     for c in data.keys():
#        table.add_column(c, [])
#     table.add_row([data.get(c, "") for c in data.keys()])
#     print(table)
#     table1 = [table]
#     Mail(data, table1)
#     return table1

def Make_table(data_dict):
    dflist = pd.DataFrame([data_dict])
    table_data_for_br = dflist
    # print("\n 6. This dataframe func has come to send_table func")
    table_for_br = build_table(table_data_for_br, 'grey_light', font_size=' 12px', font_family='Open Sans, sans-serif', text_align='left', width='auto', index=False)
    table = [table_for_br]
    Mail(data_dict ,table)
    return "Mail as Sent!!"