# Stadium Project

This project is a simulation of a stadium seat booking system implemented in C++. It allows users to register, login, pick seats, delete seats, update seats, search for available seats, and display their chosen seats.

## Files

The project consists of the following files:

- `functions.hpp`: This file contains the implementation of various classes and functions used in the stadium seat booking system.
- `script.cpp`: This file contains the main function that runs the stadium seat booking system.

## How it Works

### Seat Layout

The stadium is represented by a grid of seats, where each seat can be either available (represented by '\_') or taken (represented by 'X'). The seat layout is displayed to the user at various stages of the program.

### User Management

The system allows users to register and login. Each user has a username and password. User information is stored in a file (`users.txt`). The system loads the user information from the file at startup and saves any changes before exiting.

### Seat Management

The system keeps track of the seats chosen by users. The seat information is stored in a file (`seats.txt`). When a user picks a seat, it is marked as taken in the seat layout, and the seat number is associated with the user. Similarly, when a user deletes a seat, it is marked as available again in the seat layout, and the seat number is removed from the user's chosen seats.

### Options

The system provides the following options to the user:

1. Register: Allows a new user to register by entering a username and password. The system checks if the username is available and adds the user to the user information file.
2. Login: Allows an existing user to login by entering their username and password. The system checks if the username and password match the registered user's information.
3. Pick a seat: Allows a logged-in user to pick a seat from the stadium layout. The user can choose the row and column of the seat they want. If the seat is available, it is marked as taken, and the seat number is associated with the user.
4. Delete a seat: Allows a logged-in user to delete a previously chosen seat. The user enters the seat number they want to delete. If the seat is taken and belongs to the user, it is marked as available again, and the seat number is removed from the user's chosen seats.
5. Update a seat: Allows a logged-in user to update a previously chosen seat. The user can choose a new seat by providing the row and column. The system checks if the new seat is available and updates the user's chosen seats accordingly.
6. Search for available seats: Allows the user to search for available seats in the stadium. The user enters the row and column of the seat they want to search. The system checks if the seat is available or taken and displays the result.
7. Display your seats: Allows a logged-in user to display the seats they have chosen.
8. Exit the program: Exits the stadium seat booking system.

## How to Run

To run the program, follow these steps:

1. Compile the `script.cpp` file using a C++ compiler.

   **PowerShell:**

   ```powershell
   PS> g++ script.cpp -o stadium
   ```

   **Bash:**

   ```bash
   $ g++ script.cpp -o stadium
   ```

2. Execute the compiled program.

   **PowerShell:**

   ```powershell
   PS> ./stadium
   ```

   **Bash:**

   ```bash
   $ ./stadium
   ```
