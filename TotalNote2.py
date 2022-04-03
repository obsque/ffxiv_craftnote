import openpyxl
import pandas as pd
from Materials import Materials
from item import ITEM
import sys

직업 = ['목수', '대장', '갑주', '보석', '가죽', '재봉', '연금', '요리']

wb = openpyxl.load_workbook('./docs/제작수첩DB.xlsx')

#TotMat = []
item_dict = {}

# PRE-SCAN items - Dictionary
for sheet in wb:

    mr = sheet.max_row
    mc = sheet.max_column

    quantity = [0, 0, 0, 0, 0, 0]
    item = ["", "", "", "", "", ""]

    # ADD to dict
    for r in range(2, mr):
        name = sheet.cell(r, 4).value
        # if name not in item_dict:
        item_dict[name] = {}

        for i in range(0, 5):
            cq = i*2+5
            ci = i*2+6

            Q = sheet.cell(r,cq).value
            NAME = sheet.cell(r,ci).value
            
            if(Q != None):
                quantity[i] = Q

                if(NAME != None):
                    item[i] = NAME
                    
                    if NAME not in item_dict:
                        item_dict[NAME] = {}

                item_dict[name][NAME] = Q

# print(item_dict)

# Check and build TREE
for sheet in wb:

    quantity = [0, 0, 0, 0, 0, 0]
    item = ["", "", "", "", "", ""]
    temp_materials = {}

    mr = sheet.max_row
    mc = sheet.max_column

    for r in range(2, mr):
        if(sheet.cell(r, 1).value == None):
            # name = sheet.cell(r, 4).value
            # item_dict.popitem(name)
            continue

        name = sheet.cell(r, 4).value
        if name not in item_dict:
            item_dict[name] = {}

        for i in range(0, 5):
            cq = i*2+5
            ci = i*2+6

            Q = sheet.cell(r,cq).value
            NAME = sheet.cell(r,ci).value
            
            if(Q != None):
                quantity[i] = Q

                if(NAME != None):
                    item[i] = NAME
                    
                    if NAME not in item_dict:
                        item_dict[NAME] = {}

                    # if NAME in item_dict:
                    #     item_dict[item[i]] += quantity[i]
                    # else:
                    #     item_dict[item[i]] = quantity[i]

                item_dict[name][NAME] = Q

        

# OUTPUT #
data = pd.DataFrame(list(item_dict.items()), columns=['Name', 'Quantity'])
#print(data)
output = data.loc[data['Quantity']>0]

output.to_excel("output.xlsx")
