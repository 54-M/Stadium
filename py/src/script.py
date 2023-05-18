# time module is used in this program to add a delay between each action
import time
# import all functions from functions.py
from functions import *


def main():
  logo()
  username = None
  
  while True:
    while not username:
      print("1. Register")
      print("2. Login")
      choice = input("Enter your choice: ")
      
      if choice == "1":
        writeUser()
      elif choice == "2":
        username = loginUser()
        if username:
          print("Login successful!\n")
      else:
        print("Invalid choice. Please try again.")
      time.sleep(1)
    
    while username:
      print("1. Logout")
      print("2. Book a seat")
      print("3. View seat bookings")
      print("4. Search seat booking")
      print("5. Delete seat booking")
      print("6. Update seat booking")
      print("7. Exit")
      
      choice = input("Enter your choice: ")
      
      if choice == "1":
        print("Logged out!")
        username = None
      elif choice == "2":
        writeSeat(username)
      elif choice == "3":
        readSeat(username)
      elif choice == "4":
        searchSeat(username)
      elif choice == "5":
        deleteSeat(username)
      elif choice == "6":
        updateSeat(username)
      elif choice == "7":
        print("Exiting the program.")
        return
      else:
        print("Invalid choice. Please try again.")
      time.sleep(1)


main()
