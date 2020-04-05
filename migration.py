import MySQLdb
from migration_scripts import TABLES


def main():
  db = MySQLdb.connect(host="localhost", user="root", passwd="P@ssw0rd2019")
  
  cursor = db.cursor()

  cursor.execute("DROP DATABASE IF EXISTS boo_chat;")
  cursor.execute("CREATE DATABASE boo_chat;")
  cursor.execute("USE boo_chat;")

  cursor.execute(TABLES["accounts"])
  cursor.execute(TABLES["users"])
  cursor.execute(TABLES["rooms"])
  cursor.execute(TABLES["messages"])
  cursor.execute(TABLES["logins"])

if __name__ == "__main__":
    main()