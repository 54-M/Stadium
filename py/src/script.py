import time

users_directory = "py/data/users.txt"
seats_directory = "py/data/seats.txt"


# register user
def writeUser():
  try:
    with open(users_directory, "a+") as file:
      while True:
        username = input('Enter the username or press "q" to quit: ')
        if username == "q":
          break
        password = input("Enter the password: ")
        # Move the file cursor to the beginning of the file
        file.seek(0)
        existing_users = file.readlines()
        
        for user in existing_users:
          if username in user:
            print("Username already taken. Please choose another one.")
            break
        
        else:
          file.write(username + "\t" + password + "\n")
          print("User registered successfully!")
          break
  
  except IOError as e:
    print(f"An error occurred while writing the user: {e}")


def loginUser():
  try:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open(users_directory, "r") as file:
      for line in file:
        fields = line.split("\t")
        if fields[0] == username and fields[1].strip() == password:
          return username
    print("Invalid username or password.")
    return None
  
  except IOError as e:
    print(f"An error occurred while reading the user: {e}")


def writeSeat(username):
  try:
    with open(seats_directory, "r") as file:
      booked_seats = []
      for line in file:
        fields = line.split("\t")
        booked_seats.append(fields[1].strip())
    
    # available_seats = []
    # for seat in range(1, 100):
    #     if str(seat) not in booked_seats:
    #         available_seats.append(seat)
    
    # print("Available seats:", available_seats)
    
    with open(seats_directory, "a") as file:
      while True:
        seat_number = input(
          'Enter the seat number (1-100) or press "q" to quit: ')
        if seat_number == "q":
          break
        elif seat_number in booked_seats:
          print("This seat is already booked by another user.")
          view_available_seats = input(
            "Would you like to view available seats? (y/n): ")
          if view_available_seats.lower() == "y":
            available_seats = [seat for seat in range(1, 101) if str(seat) not in booked_seats]
            print(f"Available seats: {available_seats}")
        elif not seat_number.isdigit() or int(seat_number) < 1 or int(seat_number) > 100:
          print(
            "Invalid seat number. Please enter a number between 1 and 100.")
        else:
          file.write(username + "\t" + seat_number + "\n")
          print("Seat booked successfully!")
          break
  
  except IOError as e:
    print(f"An error occurred while writing the seat: {e}")


def readSeat(username):
  try:
    with open(seats_directory, "r") as file:
      print("Seat Numbers: ", end="")
      booked_seats = []
      for line in file:
        fields = line.split("\t")
        if fields[0] == username:
          booked_seats.append(fields[1].strip())
      
      if booked_seats:
        print(", ".join(booked_seats))
      else:
        print("No seat bookings found for this user.")
  
  except IOError as e:
    print(f"An error occurred while reading the seat: {e}")


def searchSeat(username):
  try:
    seat_number = input("Enter the seat number to search: ")
    with open(seats_directory, "r") as file:
      for line in file:
        fields = line.split("\t")
        if fields[1].strip() == seat_number:
          print(f"Seat Number: {seat_number} is booked.")
          return
    print(f"Seat number {seat_number} is available.")
  
  except IOError as e:
    print(f"An error occurred while searching the seat: {e}")


def deleteSeat(username):
  try:
    seat_number = input("Enter the seat number to delete: ")
    with open(seats_directory, "r") as file:
      lines = file.readlines()
    
    flag = False
    with open(seats_directory, "w") as file:
      for line in lines:
        fields = line.split("\t")
        if fields[0] == username and fields[1].strip() == seat_number:
          flag = True
        else:
          file.write(line)
    if flag:
      print(f"Seat number {seat_number} has been deleted.")
    else:
      print(f"Seat number {seat_number} not found or not booked by you.")
  
  except IOError as e:
    print(f"An error occurred while deleting the seat: {e}")


def updateSeat(username):
  try:
    seat_number = input("Enter the seat number to update: ")
    with open(seats_directory, "r") as file:
      lines = file.readlines()
    
    updated_lines = []
    found = False
    for line in lines:
      fields = line.split("\t")
      if fields[0] == username and fields[1].strip() == seat_number:
        new_seat_number = input("Enter the new seat number: ")
        updated_lines.append(fields[0] + "\t" + new_seat_number + "\n")
        found = True
      else:
        updated_lines.append(line)
    
    if found:
      with open(seats_directory, "w") as file:
        file.writelines(updated_lines)
      print(f"Seat number {seat_number} has been updated.")
    else:
      print(f"Seat number {seat_number} not found or not booked by you.")
  
  except IOError as e:
    print(f"An error occurred while updating the seat: {e}")


def main():
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
        break
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
