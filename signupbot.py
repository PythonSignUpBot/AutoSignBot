import openpyxl
import random
import requests
import json
 
# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("signupinfo.xlsx")
 
# Define variable to read sheet
dataframe1 = dataframe.active
 
colName = ['A', 'B', 'C', 'D', 'E', 'F']
prevPhoneNumber = ["+075 ", "+074 "]

url = 'https://app.anonaddy.com/api/v1/api-token-details'
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {GSWpykiYOoZPkBpD3U0WXbACrnSo1a1kETbkEVtq}'
}

response = requests.request('GET', url, headers=headers)
print(response.json())

Iterate the loop to read the cell values
for row in range(0, dataframe1.max_row):
    for col in dataframe1.iter_cols(1, dataframe1.max_column):
        if col[row].value == None:
            if col[row].column == 2:
                day = random.randint(1, 28)
                month = random.randint(1, 12)
                year = random.randint(1958, 1994)
                birthday = str(day) + '/' + str(month) + '/' + str(year)
                cellName = colName[col[row].column - 1]+str(row+1)
                dataframe1[cellName].value = birthday
            elif col[row].column == 6:
                prevNum = random.randint(0, 1)
                backPhoneNumber = random.randint(12345678, 98765432)
                phoneNumber = prevPhoneNumber[prevNum] + str(backPhoneNumber)
                print(phoneNumber)
                cellName = 'F' + str(row+1)
                dataframe1[cellName].value = phoneNumber
            elif col[row].column == 5:

dataframe.save("signupinfo.xlsx")