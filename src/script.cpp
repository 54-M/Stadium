#include <bits/stdc++.h>
using namespace std;

struct User {
  int id;
  char name[50], password[50];
};

struct Seat {
  int number;
  bool booked;
};

void register_user(User u) {
  ofstream file("users.txt", ios::binary | ios::app);
  file.write((char *) &u, sizeof(u));
  file.close();
  cout << "User registered successfully!" << '\n';
}

bool validation_user(char *name, char *password) {
  ifstream file("users.txt", ios::binary);
  User u;
  while (file.read((char *) &u, sizeof(u))) if (!strcmp(u.name, name) and !strcmp(u.password, password)) return true;
  file.close();
  return false;
}

void book_seat(int seat_number) {
  fstream file("seats.txt", ios::binary | ios::in | ios::out);
  Seat seat;
  file.seekg((seat_number - 1) * sizeof(Seat));
  file.read((char *) &seat, sizeof(Seat));
  if (seat.booked) {
	cout << "Seat " << seat_number << " is already booked!" << '\n';
	file.close();
	return;
  }
  seat.booked = true;
  file.seekp((seat_number - 1) * sizeof(Seat));
  file.write((char *) &seat, sizeof(Seat));
  file.close();
  cout << "Seat " << seat_number << " has been booked!" << '\n';
}

void display_available_seats() {
  ifstream file("seats.txt", ios::binary);
  Seat seat;
  cout << "Available seats:" << '\n';
  for (int i = 1; i <= 100; ++i) {
	file.read((char *) &seat, sizeof(Seat));
	if (!seat.booked) {
	  cout << i << ' ';
//	  if (!(i % 10)) cout << '\n';
	}
  }
  cout << '\n';
  file.close();
}

int main() {
  int choice, counter = 1;
  char name[50], password[50];
  User u;
  ifstream in("users.txt", ios::binary);
  if (in) {
	in.seekg(0, ios::end);
	int fileSize = in.tellg();
	if (fileSize) in.seekg(-sizeof(User), ios::end), in.read((char *) &u, sizeof(User)), counter = u.id + 1;
  }
  in.close();
  do {
	cout << "1. Register" << '\n';
	cout << "2. Login" << '\n';
	cout << "3. Book a seat" << '\n';
	cout << "4. Exit" << '\n';
	cout << "Enter your choice:";
	cin >> choice;

	switch (choice) {
	  case 1: cout << "Enter name:", cin >> u.name;
		cout << "Enter password:", cin >> u.password;
		u.id = counter++, register_user(u);
		break;
	  case 2: cout << "Enter name:", cin >> name;
		cout << "Enter password:", cin >> password;
		cout << (validation_user(name, password) ? "Login successful!\n" : "Invalid name or password!\n");
		break;
	  case 3: {
		if (!validation_user(name, password)) {
		  cout << "You need to log in first!" << '\n';
		  break;
		}
		bool seats[100] = {false};
		ifstream seatFile("seats.txt", ios::binary);
		if (seatFile) seatFile.read((char *) &seats, sizeof(seats));
		seatFile.close();
		cout << "Available seats:" << '\n';
		for (int i = 0; i < 100; ++i) {
		  if (!seats[i]) {
			cout << i + 1 << ' ';
			if (i > 1 and !((i + 1) % 10)) cout << '\n';
		  }
		}
		cout << '\n';
		int seat_number;
		cout << "Enter the seat number you want to book:", cin >> seat_number;
		if (seat_number < 1 or seat_number > 100) {
		  cout << "Invalid seat number!" << '\n';
		  break;
		}
		if (seats[seat_number - 1]) {
		  cout << "Sorry, this seat is already booked." << '\n';
		  break;
		}
		seats[seat_number - 1] = true;
		ofstream seatFileOut("seats.txt", ios::binary);
		seatFileOut.write((char *) &seats, sizeof(seats));
		seatFileOut.close();
		cout << "Seat " << seat_number << " booked successfully!" << '\n';
		break;
	  }
	  case 4: cout << "Thank you for using the system, hope see you again." << '\n';
		break;
	  default: cout << "Invalid choice." << '\n';
		break;
	}
  } while (choice != 4);
}