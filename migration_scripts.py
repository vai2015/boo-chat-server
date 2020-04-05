TABLES:dict = {
  "accounts": """
    CREATE TABLE accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        salt VARCHAR(255) NOT NULL,
        hash VARCHAR(255) NOT NULL
    );
  """,
  "users": """
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        status TEXT,
        FOREIGN KEY(account_id) REFERENCES accounts(id)
    );
  """,
  "rooms": """
    CREATE TABLE rooms (
          id INT AUTO_INCREMENT PRIMARY KEY,
          user_id INT NOT NULL,
          code VARCHAR(255) NOT NULL,
          FOREIGN KEY(user_id) REFERENCES accounts(id)
    );
  """,
  "messages": """
     CREATE TABLE messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        room_id INT NOT NULL,
        sender_id INT NOT NULL,
        receiver_id INT NOT NULL,
        is_read BOOLEAN DEFAULT FALSE,
        message TEXT NOT NULL,
        created_date TIMESTAMP NOT NULL,
        read_date TIMESTAMP DEFAULT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms(id),
        FOREIGN KEY (sender_id) REFERENCES users(id),
        FOREIGN KEY (receiver_id) REFERENCES users(id)
    );
  """,
  "logins": """
    CREATE TABLE logins (
      id INT AUTO_INCREMENT PRIMARY KEY,
      account_id INT NOT NULL,
      login_date TIMESTAMP NOT NULL,
      is_logged_in BOOLEAN DEFAULT FALSE
    );
  """
}
