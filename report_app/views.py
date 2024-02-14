from django.db import connection
from django_query_to_table import DjangoQtt
from django.http import HttpResponse

# View function in Django project
def listOfOrders(request):
  cursor = connection.cursor()
  reportTitle = "Order List"
  sqlQuery = "SELECT order_number AS 'No.', order_item AS 'Item', total_amount AS 'Price', order_date AS 'Date' FROM report_app_order"
  columnsToBeSummarized = ['Price']
  fontName = "Arial"
  cssClasses = "reportTable container"
  headerRowBackgroundColor = '#ffeeee'
  evenRowsBackgroundColor = '#ffeeff'
  oddRowsBackgroundColor = '#ffffff'
  table = DjangoQtt.generateFromSql(cursor, reportTitle, sqlQuery, columnsToBeSummarized, cssClasses,
                                  "ltr", fontName, "Total Price", True,
                                  headerRowBackgroundColor, evenRowsBackgroundColor, oddRowsBackgroundColor
                                  )
  # table is a string variable contianing the html table showing the query result
  return HttpResponse(table)
