from subprocess import call
# https://pypi.python.org/pypi/tabulate
from tabulate import tabulate
# mysql.connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation-source.html
import mysql.connector

# database initialize
database = mysql.connector.connect(user = "root", password = "password",
  host = "localhost", database = "sekretariat")
cursor = database.cursor()

def add():
  call("clear")
  query = "SELECT * FROM contractors ORDER BY id"
  cursor.execute(query)
  print(26 * "#" + "\n#   NOWY PRZESTAWICIEL" + "   #\n" + 26 * "#")
  print()
  for (id, name) in cursor:
    print(str(id) + "\t" + name)
  contractor_id = input("\nWybierz numer kontrahenta, któremu chcesz dodać przedstawiciela: ")

  cursor.execute("SELECT id FROM contractors WHERE id = %s", (contractor_id, ))

  if not cursor.fetchone():
    print("Taki kontrahent nie instnieje")
    return
  call("clear")

  first_name = input("Podaj imię przedstawiciela: ")

  if len(first_name) == 0:
    while len(first_name) == 0:
      print("\nImię nie może być puste.")
      first_name = input("Podaj imię przedstawiciela: ")

  call("clear")

  last_name = input("Podaj nazwisko przedstawiciela: ")

  if len(last_name) == 0:
    while len(last_name) == 0:
      print("\nNazwisko nie może być puste.")
      last_name = input("Podaj nazwisko przedstawiciela: ")

  call("clear")

  email = input("Podaj email przedstawiciela: ")

  if len(email) == 0:
    while len(email) == 0:
      print("\nEmail nie może być pusty.")
      email =input("Podaj email przedstawiciela: ")

  q = ("INSERT INTO representatives (contractor_id, first_name, last_name, email) "
      "VALUES (%s, %s, %s, %s)")
  cursor.execute(q, (contractor_id, first_name, last_name, email))

  call("clear")
  print("Przedstawiciel został dodany.\n")
  input("Naciśnij ENTER aby kontynuować...")
  database.commit()

def list():
  query = ("SELECT CONCAT(r.first_name, ' ',r.last_name) AS full_name, r.email, c.name AS name"
           " FROM representatives r JOIN contractors c ON c.id = r.contractor_id")
  cursor.execute(query)

  print(24 * "#" + "\n#   KSIĄŻKA ADRESOWA " + "  #\n" + 24 * "#")

  print()
  print(tabulate(cursor, headers=["PRZEDSTAWICIEL", "EMAIL", "KONTRAHENT"]))
  input("\nNaciśnij ENTER aby kontynuować...")
