# from pretty_html_table import build_table
from prettytable import PrettyTable


# Create your tests here.
data = {'User Name': 'Sourabh Gupta', 'User Email': 'Sourabh.gupta@rampgroup.com', 'Build Name': 'High_RTOSApp_SingleApp_QNX', 'Branch Name': 'develop', 'Commit ID': '', 'DisplaySet': 'FF_High', 'System': 'R2-PATAC', 'Build Mode': 'debug', 'Jira Ticket Link': 'https://sourabh.gupta.com', 'Comment': 'This is test for the Mail Agent :))'}

def table_agent_mail(data):
    table = PrettyTable()
    for c in data.keys():
       table.add_column(c, [])
    table.add_row([data.get(c, "") for c in data.keys()])
    print(table)
    table = [table]
    return table

table_agent_mail(data)