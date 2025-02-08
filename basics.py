import pandas as pd

# data = {
#     'Name': ['Bhuvnesh','Praveen','Prajwal','Gopal','Niharika','Disha'],
#     'Age': ['35','30','28','34','33','28'],
#     'City': ['Nagavara','gurguntepalya','Rajajinagar','Mahalaxmilayout','Peenya','Rajajinagar']
# }
#
# df = pd.DataFrame(data)
# print(df)
# Write DataFrame to an Excel file
# df.to_excel('people.xlsx', index=False)

# Read data from excel file
file = pd.read_excel('people.xlsx')
#
print(file)

# new data to append a file
# new_data = {
#     'Name' : ['tamilarasu'],
#     'Age':['30'],
#     'city':['guruguntepalya']
# }
#
# new_df = pd.DataFrame(new_data)
# print(new_df)

#append to an existing file
# with pd.ExcelWriter('people.xlsx',mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
#     new_df.to_excel(writer,index=False, header=False)