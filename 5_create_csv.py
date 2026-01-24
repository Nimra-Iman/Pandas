# DIFFERENCE BETWEEN csv and xls files:
    # CSV(Comma Separated values):
        # plain text format in which values are separated by comma
                # name,age,city
                # John,30,New York
                # Jane,25,Los Angeles
        # CSV files only store the raw data and do not support any formatting like 
        # fonts, colors, or cell styles.

    # XLS (excel file):
        # edxcel sheet buinary file format that holds information about all the worksheets
        # in the file, inclusing both content and formatting.

# CSV: Good for simple, plain text data storage and easy to read by most software.
# XLS: Ideal for complex data storage with multiple sheets and formatting options.

#   CSV IS ACTUALLY SIMPLE PLAIN TEXT SEPARATED BY COMMA AND DO NOT SUPPORT FORMATTING, WHEN WE OPEN IT IN EXCEL,
# IT IS PROPERTY OF EXECL K VO US KO CHCEK KRTA H OR ELEMENTS KO DIFFERENT ROWS M SHOW KRTA H
# CHAHY CHECK KR LO K EXCEL M HI IS CSV FILE KO KUCH BOLD KRO, KUCH COLOR ETC CHNAGE KRO AND THEN USI FILE KO 
# NOTEBPAD M OPEN KRO TO SAARI FORMATTING JA CHUKI HO GI Q K VO FORATING EXCEL N SAVE KI HUI THI, .CSV FILE N
# NHI KI HUI THI,, SIMILARLY .XLS KO NOTEPAD M OPEN KRO GY TO KUCH BINARY OR ENCRYPTED TEXT AY GA  

# ----------------  CREATING A CSV FILE:
import pandas as pd

x={"name":["nimra","iman"], "age":[21,23]}
data=pd.DataFrame(x)
# print(data)
# data.to_csv("my_csvfile.csv")  #now the csv file is created.
data.to_csv("my_csvfile1.csv", index=False, header=["a","b"])  #now the csv file is created.

