import pyodbc
import azure.functions as func
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    cardCode = req.get_json()
    cardCodestring = str(cardCode["cardCode"])
    peopleConString = os.getenv('PeopleConString')

    with pyodbc.connect(peopleConString) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cardcode from People where cardcode = %s" % cardCodestring)
            row = cursor.fetchone()
            flag = 0
            while row:
                if cardCodestring == row[0]:
                    flag = 1
                    break
                row = cursor.fetchone()
            if flag == 0:
                cursor.execute("insert into People VALUES('%s')" % cardCodestring)
                return func.HttpResponse("dodano ", status_code=302)
            if flag == 1:
                return func.HttpResponse("obiekt istnieje w bazie ", status_code=418)

            

                
        
