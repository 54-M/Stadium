#include <bits/stdc++.h>
#include <windows.h>
//medhat
#include "../includes/functions.hpp"

using namespace std;

int main() {
  users_directory = "../data/users.txt";
  seats_directory = "../data/seats.txt";

  int choice;
  stadium = new Stadium(10, 10);
  load_users(), load_seats();
  user_info *current_user = 0;
  logo();
  cout << "\n ----------------------------------------------\n";
  cout << "|  Welcome to the stadium seat booking system  |\n";
  cout << " ----------------------------------------------\n";

  bool flag = 1;
  while (flag) {
    cout << "\nPlease choose an option:\n";
    cout << "------------------------------\n";
    cout << "1. Register\n";
    cout << "2. Login\n";
    cout << "3. Pick a seat\n";
    cout << "4. Delete a seat\n";
    cout << "5. Update a seat\n";
    cout << "6. Search for available seats\n";
    cout << "7. Display your seats\n";
    cout << "8. Exit the program\n";
    cout << "------------------------------\n";
    cout << "Your choice: ";

    cin >> choice;
    switch (choice) {
      case 1:
        register_user();
        Sleep(1000);
        break;
      case 2:
        current_user = login_user();
        Sleep(1000);
        break;
      case 3:
        pick_seat(current_user);
        Sleep(1000);
        break;
      case 4:
        delete_seat(current_user);
        Sleep(1000);
        break;
      case 5:
        update_seat(current_user);
        Sleep(1000);
        break;
      case 6:
        search_seats();
        Sleep(1000);
        break;
      case 7:
        display_seats(current_user);
        Sleep(1000);
        break;
      case 8:
        flag = 0;
        break;
      default:
        cout << "Invalid option.\n";
        Sleep(1000);
    }
  }
  save_users(), save_seats(), delete stadium;
  cout << "Have fun. Goodbye.\n";
}
