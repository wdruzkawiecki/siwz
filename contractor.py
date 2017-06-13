from subprocess import call

# mysql.connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation-source.html
import mysql.connector

# database initialize
database = mysql.connector.connect(user = "root", password = "password",
  host = "localhost", database = "sekretariat")
cursor = database.cursor()

# zapytania do tabeli contracotrs
def add():
  query = "INSERT INTO contractors(name) VALUES(%s)"
  call("clear")
  print(23 * "#" + "\n#   NOWY KONTRAHENT" + "   #\n" + 23 * "#")
  print()
  new_conractor_name = input("Podaj nazwę kontrahenta: ")

  if len(new_conractor_name) == 0:
    while len(new_conractor_name) == 0:
      print("\nNazwa nie może być pusta.")
      new_conractor_name = input("Podaj nazwę kontrahenta: ")

  print("Zapisywanie...")
  try:
    cursor.execute(query, (new_conractor_name, ))
  except mysql.connector.Error as e:
    if e.errno == 1062:
      call("clear")
      print("Kontrahent o podanej nazwie już istnieje.\n")
      input("Naciśnij ENTER aby kontynuować...")
      return
    else:
      print("Wystapił błąd. Spróbuj ponownie.")
      return
  call("clear")
  print("Kontrahent został dodany.\n")
  input("Naciśnij ENTER aby kontynuować...")
  database.commit()

def list():
  call("clear")
  print(19 * "#" + "\n#   KONTRAHENCI" + "   #\n" + 19 * "#")
  query = "SELECT * FROM contractors"
  cursor.execute(query)
  print()
  for (id, name) in cursor:
    print(name)
  input("\nNaciśnij ENTER aby kontynuować...")
