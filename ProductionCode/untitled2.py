from database import *
databite = "SELECT agr_total FROM GLOBALDATA_S WHERE yr = " + '2004' + " AND country = ’"+ 'France' +"’;"
data2 = DataSource.run_string_psql(databite)
print(data2)