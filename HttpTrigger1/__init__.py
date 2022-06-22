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
            try:
                cursor.execute("SELECT cardcode from People where cardcode = %s" % cardCodestring)
                return func.HttpResponse('Dobra karta', status_code=302) 
                
            except:
                return func.HttpResponse("zla karta", status_code=418)
