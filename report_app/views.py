from django.shortcuts import render

from django.db import connection
from django_query_to_table import DjangoQtt
from django.http import HttpResponse

# view function in Django project
def listOfOrders(request):
  cursor = connection.cursor()
  reportTitle = "Order List"
  sqlQuery = "SELECT order_number, order_item, total_amount, order_date FROM report_app_order"
  columnsToBeSummarized = ['total_amount']
  fontName = "Arial"
  cssClasses = "reportTable container"
  headerRowBackgroundColor = '#ffeeee'
  evenRowsBackgroundColor = '#ffeeff'
  oddRowsBackgroundColor = '#ffffff'
  table = DjangoQtt.generateFromSql(cursor, reportTitle, sqlQuery, columnsToBeSummarized, cssClasses,
                                  "ltr", fontName, "Total amount", True,
                                  headerRowBackgroundColor, evenRowsBackgroundColor, oddRowsBackgroundColor
                                  )
  # table is a string variable contianing the html table showing the query result

  return HttpResponse(table)