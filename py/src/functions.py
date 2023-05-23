import os

users_directory = "py/data/users.txt"
seats_directory = "py/data/seats.txt"

# register user
def writeUser():
  try:
    with open(users_directory, "a+") as file:
      while True:
        username = input('Enter the username or press "q" to quit: ')
        if username == "q": break
        password = input("Enter the password: ")
        # Move the file cursor to the beginning of the file
        file.seek(0)
        existing_users = file.readlines()
        
        for user in existing_users:
          if username in user:
            print("Username already taken. Please choose another one.")
            break
        
        else:
          file.write(f"{username}\t{password}\n")
          print("User registered successfully!")
          break
  
  except IOError as e:
    print(f"An error occurred while writing the user: {e}")

# login user
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

# book a seat
def writeSeat(username):
  try:
    with open(seats_directory, "r") as file:
      booked_seats = []
      for line in file:
        fields = line.split("\t")
        booked_seats.append(fields[1].strip())
    
    with open(seats_directory, "a") as file:
      while True:
        seat_number = input('Enter the seat number (1-100) or press "q" to quit: ')
        if seat_number == "q":
          break
        elif seat_number in booked_seats:
          print("This seat is already booked by another user.")
          view_available_seats = input("Would you like to view available seats? (y/n): ")
          if view_available_seats.lower() == "y":
            available_seats = []
            for seat in range(1, 101):
              if str(seat) not in booked_seats:
                available_seats.append(seat)
            print(f"Available seats: {available_seats}")
        elif not seat_number.isdigit() or int(seat_number) < 1 or int(seat_number) > 100:
          print("Invalid seat number. Please enter a number between 1 and 100.")
        else:
          file.write(f"{username}\t{seat_number}\n")
          print("Seat booked successfully!")
          break
  
  except IOError as e:
    print(f"An error occurred while writing the seat: {e}")

# view seat bookings
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
        # join() method returns a string in which the elements of sequence have been joined by str separator.
        print(", ".join(booked_seats))
      else:
        print("No seat bookings found for this user.")
  
  except IOError as e:
    print(f"An error occurred while reading the seat: {e}")

# search for a seat and check if it is booked
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

# delete a seat
def deleteSeat(username):
  try:
    
    seat_number = input("Enter the seat number to delete: ")
    
    # with open("py/data/seats_temp.txt", "w") as temp:
    #   with open(seats_directory, "r") as file:
    #     for line in file:
    #       field = line.split('\t')
    #       if seat_number != field[1].strip():
    #         temp.write(line)
  
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
    
    
    
    # os.remove(seats_directory)
    # os.rename("py/data/seats_temp.txt", "py/data/seats.txt")
  except IOError as e:
    print(f"An error occurred while deleting the seat: {e}")

# update a seat
def updateSeat(username):
  try:
    seat_number = input("Enter the seat number to update: ")
    with open(seats_directory, "r") as file:
      lines = file.readlines()
    
    updated_lines = []
    flag = False
    for line in lines:
      fields = line.split("\t")
      if fields[0] == username and fields[1].strip() == seat_number:
        new_seat_number = input("Enter the new seat number: ")
        updated_lines.append(f"{username}\t{new_seat_number}\n")
        flag = True
      else:
        updated_lines.append(line)
    
    if flag:
      with open(seats_directory, "w") as file:
        file.writelines(updated_lines)
      print(f"Seat number {seat_number} has been updated.")
    else:
      print(f"Seat number {seat_number} not found or not booked by you.")
  
  except IOError as e:
    print(f"An error occurred while updating the seat: {e}")


def logo():
  colore_1 = "\033[33m"
  colore_2 = "\033[31m"
  reset_colore = "\033[0m"
  
  print("                                                                  ")
  print("                                                                  ")
  print("                                                                  ")
  print("                            " + colore_1 + ".:------:. " + reset_colore + "                            ")
  print("                      " + colore_1 + ":=*%@@@@@@@@@@@@@@%*=:" + reset_colore + "                      ")
  print("                  " + colore_1 + ".=#@@@@@@@@@@@@@@@@@@@@@@@@#=." + reset_colore + "                  ")
  print("                " + colore_1 + "-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=" + reset_colore + "                ")
  print("              " + colore_1 + "=@@@@@@@@@@@@@@@@@@@@@@@#+=--=+#@@@@@+" + reset_colore + "              ")
  print("            " + colore_1 + ".%@@@@@@@@@@@@@@@@@@@@@*:          -#@@@@-" + reset_colore + "            ")
  print("              " + colore_1 + ":=*%@@@@@@@@@@@@@@@%.      ..      :@@@@*" + reset_colore + "           ")
  print("                   " + colore_1 + ":=*%@@@@@@@@@%     =%@@@@#-    .@@@@%" + reset_colore + "          ")
  print("         " + colore_2 + "#@#+-." + reset_colore + "         " + colore_1 + ":-*%@@@@=    +@@@@@@@@-    *@@@@%" + reset_colore + "         ")
  print("        " + colore_2 + "=@@@@@@@#+-." + reset_colore + "         " + colore_1 + ".-+     @@@@@@@@@=    *@@@@@*" + reset_colore + "        ")
  print("        " + colore_2 + "@@@@@@@@@@@@@#+-." + reset_colore + "           " + colore_1 + ":#@@@@@@@+     @@@@@@@:" + reset_colore + "       ")
  print("       " + colore_2 + "=@@@@@@@@@@@@@@@@@@#+-:" + reset_colore + "         " + colore_1 + ".-==:     .%@@@@@@@*" + reset_colore + "       ")
  print("       " + colore_2 + "*@@@@@@@@@@@@@@@@@@@@@@@" + reset_colore + "                 " + colore_1 + "=@@@@@@@@@%" + reset_colore + "       ")
  print("       " + colore_2 + "#@@@@@@@@@@@%*=::::-+*%*" + reset_colore + "    " + colore_1 + "=%*=:...:-=#@@@@@@@@@@@@" + reset_colore + "       ")
  print("       " + colore_2 + "#@@@@@@@@@*." + reset_colore + "                " + colore_1 + "#@@@@@@@@@@@@@@@@@@@@@@%" + reset_colore + "       ")
  print("       " + colore_2 + "=@@@@@@@@:     .--:." + reset_colore + "         " + colore_1 + ".-+#@@@@@@@@@@@@@@@@@@*" + reset_colore + "       ")
  print("       " + colore_2 + ".@@@@@@@:    -%@@@@@@#-" + reset_colore + "           " + colore_1 + ".-+#%@@@@@@@@@@@@:" + reset_colore + "       ")
  print("        " + colore_2 + "+@@@@@%    :@@@@@@@@@.    +=:" + reset_colore + "          " + colore_1 + "-+#@@@@@@@*" + reset_colore + "        ")
  print("         " + colore_2 + "#@@@@%    :@@@@@@@@#    :@@@@%*=:" + reset_colore + "         " + colore_1 + ".-+#@%" + reset_colore + "         ")
  print("          " + colore_2 + "#@@@@:    -%@@@@@*     #@@@@@@@@@%*=:" + reset_colore + "                   ")
  print("           " + colore_2 + "*@@@@-     .::.      *@@@@@@@@@@@@@@@%*=:" + reset_colore + "              ")
  print("            " + colore_2 + "-@@@@#:           =@@@@@@@@@@@@@@@@@@@@@@-" + reset_colore + "            ")
  print("              " + colore_2 + "+@@@@@*=----=+%@@@@@@@@@@@@@@@@@@@@@@*." + reset_colore + "             ")
  print("                " + colore_2 + "=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+." + reset_colore + "               ")
  print("                  " + colore_2 + ".+%@@@@@@@@@@@@@@@@@@@@@@@@%+:" + reset_colore + "                  ")
  print("                      " + colore_2 + "-+#%@@@@@@@@@@@@@@@#+-." + reset_colore + "                     ")
  print("                            " + colore_2 + "':-------:'" + reset_colore + "                           ")
  print("                                                                  ")
  print("                                                                  ")
  print("                                                                  ")