#include <bits/stdc++.h>
using namespace std;

class user_info {
 public:
  vector<int> seats;
  string username, password;
  user_info(string u, string p) : username(u), password(p) {}
};

class Stadium {
 public:
  int rows, cols;
  vector<vector<bool>> seats;
  Stadium(int r, int c) {
	rows = r, cols = c;
	seats.resize(rows);
	for (int i = 0; i < rows; i++) seats[i].resize(cols, true);
  }

  void display() {
	cout << "Stadium layout:\n";
	cout << "   ";
	for (int j = 0; j < cols; j++) cout << j + 1 << " ";
	cout << "\n";
	for (int i = 0; i < rows; i++) {
	  cout << i + 1 << (i == rows - 1 ? " " : "  ");
	  for (int j = 0; j < cols; j++) cout << (seats[i][j] ? "_ " : "X ");
	  cout << '\n';
	}
  }

  bool is_available(int r, int c) {
	return seats[r][c];
  }

  void take_seat(int r, int c) {
	seats[r][c] = false;
  }

  void free_seat(int r, int c) {
	seats[r][c] = true;
  }
};

map<string, user_info *> users_map; // store the users_map
Stadium *stadium; // store the stadium

void load_users() {
  ifstream in("users.txt");
  if (in.fail()) return void(cout << "Failed to open users_map file\n");
  string u, p;
  while (in >> u >> p) {
	user_info *user = new user_info(u, p);
	users_map[u] = user;
  }
  in.close();
}

void save_users() {
  ofstream out("users.txt");
  if (out.fail()) return void(cout << "Failed to open users file\n");
  for (auto it : users_map) out << it.first << " " << it.second->password << "\n";
  out.close();
}

void load_seats() {
  ifstream in("seats.txt");
  if (in.fail()) return void(cout << "Failed to open seats file\n");
  string u;
  int s;
  while (in >> u >> s) {
	user_info *user = users_map[u];
	if (user != nullptr) {
	  user->seats.push_back(s);
	  int r = (s - 1) / stadium->cols, c = (s - 1) % stadium->cols;
	  stadium->take_seat(r, c);
	}
  }
  in.close();
}

void delete_seat(user_info *user) {
  if (!user) return void(cout << "You need to login first.\n");
  if (user->seats.empty()) return void(cout << "You have not picked any seats yet.\n");
  int s;
  cout << "Enter the seat number you want to delete: ";
  cin >> s;
  int r = (s - 1) / stadium->cols, c = (s - 1) % stadium->cols;
  if (r < 0 or r >= stadium->rows or c < 0 or c >= stadium->cols) return void(cout << "Invalid seat number.\n");

  if (stadium->is_available(r, c)) return void(cout << "You have not picked that seat.\n");
  stadium->free_seat(r, c);
  for (auto it = user->seats.begin(); it != user->seats.end(); it++) {
	if (*it == s) {
	  user->seats.erase(it);
	  break;
	}
  }
  cout << "You have deleted seat number " << s << ".\n";
}

void save_seats() {
  ofstream out("seats.txt");
  if (out.fail()) return void(cout << "Failed to open seats.txt\n");
  for (auto it : users_map) for (int s : it.second->seats) out << it.first << " " << s << "\n";
  out.close();
}

void register_user() {
  string u, p;
  cout << "Enter a username: ", cin >> u;
  cout << "Enter a password: ", cin >> p;
  if (users_map.count(u) > 0) return void(cout << "Sorry, that username is already taken.\n");
  user_info *user = new user_info(u, p);
  users_map[u] = user, cout << "Registration successful.\n";
}

user_info *login_user() {
  string u, p;
  cout << "Enter your username: ", cin >> u;
  cout << "Enter your password: ", cin >> p;
  if (users_map.count(u) == 0) return cout << "Sorry, that username does not exist.\n", nullptr;
  user_info *user = users_map[u];
  if (user->password != p) return cout << "Sorry, that password is incorrect.\n", nullptr;
  cout << "Login successful.\n";
  return user;
}

void pick_seat(user_info *user) {
  if (!user) return void(cout << "You need to login first.\n");
  stadium->display();
  int r, c;
  cout << "Enter the row number of the seat you want to pick: ", cin >> r;
  cout << "Enter the column number of the seat you want to pick: ", cin >> c;
  r--, c--;
  if (r < 0 or r >= stadium->rows or c < 0 or c >= stadium->cols) return void(cout << "Invalid seat number.\n");
  if (!stadium->is_available(r, c)) return void(cout << "Sorry, that seat is already taken.\n");
  stadium->take_seat(r, c);
  int s = r * stadium->cols + c + 1;
  user->seats.push_back(s);
  cout << "You have picked seat number " << s << ".\n";
}

void update_seat(user_info *user) {
  if (!user) return void(cout << "You need to login first.\n");
  if (user->seats.empty()) return void(cout << "You have not picked any seats yet.\n");
  int s;
  cout << "Enter the seat number you want to update: ", cin >> s;
  int r = (s - 1) / stadium->cols, c = (s - 1) % stadium->cols;
  if (r < 0 or r >= stadium->rows or c < 0 or c >= stadium->cols) return void(cout << "Invalid seat number.\n");
  if (stadium->is_available(r, c)) return void(cout << "You have not picked that seat.\n");
  for (auto it = user->seats.begin(); it != user->seats.end(); it++) {
	if (*it == s) {
	  user->seats.erase(it);
	  break;
	}
  }
  stadium->free_seat(r, c);
  pick_seat(user);
}

void search_seats() {
  int r, c;
  cout << "Enter the row number of the seat you want to search: ", cin >> r;
  cout << "Enter the column number of the seat you want to search: ", cin >> c, r--, c--;
  if (r < 0 or r >= stadium->rows or c < 0 or c >= stadium->cols) return void(cout << "Invalid seat number.\n");
  cout << (stadium->is_available(r, c) ? "That seat is available.\n" : "That seat is taken.\n");
}
void display_seats(user_info *user) {
  if (!user) return void(cout << "You need to login first.\n");
  if (user->seats.empty()) return void(cout << "You have not picked any seats yet.\n");
  cout << "Your seats are: ";
  for (int s : user->seats) cout << s << ", ";
  cout << "\n";
}

void display_menu() {
  cout << "\n ----------------------------------------------\n";
  cout << "|  Welcome to the stadium seat booking system  |\n";
  cout << " ----------------------------------------------\n\n";
  cout << "Please choose an option:\n";
  cout << "--------------------------\n";
  cout << "1| Register\n";
  cout << "2| Login\n";
  cout << "3| Pick a seat\n";
  cout << "4| Delete a seat\n";
  cout << "5| Update a seat\n";
  cout << "6| Search for available seats\n";
  cout << "7| Display your seats\n";
  cout << "8| Exit the program\n";
  cout << "--------------------------\n";
  cout << "Your choice: ";
}

int main() {
  int choice;
  stadium = new Stadium(10, 10);
  load_users(), load_seats();
  user_info *currentUser = nullptr;
  display_menu(), cin >> choice;
  while (choice != 8) {
	switch (choice) {
	  case 1: register_user();
		break;
	  case 2: currentUser = login_user();
		break;
	  case 3: pick_seat(currentUser);
		break;
	  case 4: delete_seat(currentUser);
		break;
	  case 5: update_seat(currentUser);
		break;
	  case 6: search_seats();
		break;
	  case 7: // Added this case
		display_seats(currentUser);
		break;
	  default: cout << "Invalid option.\n";
	}
	display_menu();
	cin >> choice;
  }
  save_users(), save_seats(), delete stadium;
  cout << "Have fun. Goodbye.\n";
}