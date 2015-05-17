import csv

with open('text.csv') as dbase:
    terms={}
    dbtext=csv.reader(dbase)
    for row in dbtext:
        terms[row[0]]=row[1:]
