from subprocess import call
import contractor as contractor
import representative as representative
import sys

while True:
  call("clear")

  # banner
  print(15 * "#" + "\n#   REJESTR" + "   #\n" + 15 * "#")

  # menu
  print("\n### MENU ###")
  print("1. Wyświetl kontrahentów")
  print("2. Dodaj kontrahenta")
  print("3. Dodaj przedstawiciela")
  print("4. Generuj ksiązke adresową")
  print("5. Wyjście\n\n")

  # pobieramy opcje od uzytkownika
  option = input("Wybierz opcję: ")

  if option == "1":
    contractor.list()
  elif option == "2":
    contractor.add()
  elif option == "3":
    representative.add()
  elif option == "4":
    representative.list()
  elif option == "5":
    sys.exit()
