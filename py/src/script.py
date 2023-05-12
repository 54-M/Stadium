users_directory = "py/data/users.txt"
seats_directory = "py/data/seats.txt"


def writeUser():
    with open(users_directory, "a") as file:
        while True:
            username = input('Enter the username or press "q" to quit: ')
            if username == "q":
                break
            password = input('Enter the password: ')
            file.write(username + '\t' + password + '\n')


def readUser():
    with open(users_directory, "r") as file:
        print('Username\tPassword')
        for line in file:
            print(line, end='')


def loginUser():
    username = input('Enter the username: ')
    password = input('Enter the password: ')
    with open(users_directory, "r") as file:
        for line in file:
            fields = line.split('\t')
            if fields[0] == username and fields[1].strip() == password:
                print('Login successful!')
                return username  # Return the logged-in username
    print('Invalid username or password.')
    return None


def writeSeatBooking(username):
    if not username:
        print('Please log in to book a seat.')
        return

    with open(seats_directory, "a") as file:
        while True:
            seat_number = input('Enter the seat number or press "q" to quit: ')
            if seat_number == "q":
                break
            file.write(username + '\t' + seat_number + '\n')


def readSeatBooking(username):
    if not username:
        print('Please log in to view seat bookings.')
        return

    with open(seats_directory, "r") as file:
        print('Seat Numbers:', end='')
        booked_seats = []
        for line in file:
            fields = line.split('\t')
            if fields[0] == username:
                booked_seats.append(fields[1].strip())

        if booked_seats:
            print(', '.join(booked_seats))
        else:
            print('No seat bookings found for this user.')


def searchSeatBooking(username):
    if not username:
        print('Please log in to search seat bookings.')
        return

    seat_number = input('Enter the seat number to search: ')
    with open(seats_directory, "r") as file:
        for line in file:
            fields = line.split('\t')
            if fields[1].strip() == seat_number:
                print(f'Seat Number: {seat_number} is booked.')
                return
    print(f'Seat number {seat_number} is available.')


def deleteSeatBooking(username):
    if not username:
        print('Please log in to delete a seat booking.')
        return

    seat_number = input('Enter the seat number to delete: ')
    with open(seats_directory, "r") as file:
        lines = file.readlines()

    flag = False
    with open(seats_directory, "w") as file:
        for line in lines:
            fields = line.split('\t')
            if fields[0] == username and fields[1].strip() == seat_number:
                flag = True
            else:
                file.write(line)
    if flag:
        print(f'Seat number {seat_number} has been deleted.')
    else:
        print(f'Seat number {seat_number} not found or not booked by you.')


def updateSeatBooking(username):
    if not username:
        print('Please log in to update a seat booking.')
        return
    seat_number = input('Enter the seat number to update: ')
    with open(seats_directory, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    found = False
    for line in lines:
        fields = line.split('\t')
        if fields[0] == username and fields[1].strip() == seat_number:
            new_seat_number = input('Enter the new seat number: ')
            updated_lines.append(fields[0] + '\t' + new_seat_number + '\n')
            found = True
        else:
            updated_lines.append(line)

    if found:
        with open(seats_directory, 'w') as file:
            file.writelines(updated_lines)
        print(f'Seat number {seat_number} has been updated.')
    else:
        print(f'Seat number {seat_number} not found or not booked by you.')


def main():
    username = None

    while True:
        print('1. Register')
        print('2. Login')
        print('3. Book a seat')
        print('4. View seat bookings')
        print('5. Search seat booking')
        print('6. Delete seat booking')
        print('7. Update seat booking')
        print('8. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            writeUser()
        elif choice == '2':
            username = loginUser()
            if username:
                print('Login successful!')
        elif choice == '3':
            writeSeatBooking(username)
        elif choice == '4':
            readSeatBooking(username)
        elif choice == '5':
            searchSeatBooking(username)
        elif choice == '6':
            deleteSeatBooking(username)
        elif choice == '7':
            updateSeatBooking(username)
        elif choice == '8':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please try again.')


main()
