import pandas as pd


def BuildRequestExcel(data_dict : list):

    df = pd.DataFrame(data_dict)
    # df=df.drop(['index'])
    print(df)
    try:
        # append_df_to_excel(df, fr"C:/Users/SourabhGupta/PycharmProjects/Form Portal/Forms/formapp/Excels/Build request.xlsx")
        append_df_to_excel(df, "C:\\Users\\SourabhGupta\\PycharmProjects\\Forms\\formapp\\Excels\\Build request.xlsx")
    except Exception as e:
        print(e)

def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)

    del df_excel['Index']
    # df_excel.drop(['S.NO'])

    # result = pd.concat([df_excel, df]).set_index('Index')
    # result = pd.concat([df_excel, df], ignore_index=True).drop_duplicates(subset = ['Developer_Email_ID', 'Repo', 'Date_Time', 'Jira ID', 'Status'],keep='last')
    result = pd.concat([df_excel, df], ignore_index=True)
    print(result)
    result.to_excel(excel_path, index=True, index_label='Index')
