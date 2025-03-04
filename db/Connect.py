import pyodbc


cnxn = pyodbc.connect(
    driver="{ODBC Driver 18 for SQL Server}",
    server="192.168.109.215",
    database="Utility",
    uid="sa",
    pwd="Camlab110",
    port=1433,
    TrustServerCertificate="yes",
)

cursor = cnxn.cursor()
print("hello")

