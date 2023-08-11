import openpyxl
import random
import requests
import json
 
# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("signupinfo.xlsx")
# Define variable to read sheet
dataframe1 = dataframe.active
for row in range(1, dataframe1.max_row):
  for col in dataframe1.iter_cols(1, dataframe1.max_column):
    if col[row].column == 1:
      vName = col[row].value
      print(vName)