import sqlite3

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()

def add_user(conn, username, password):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print(f"Kullanıcı '{username}' başarıyla eklendi.")
    except sqlite3.IntegrityError:
        print("Bu kullanıcı adı zaten alınmış.")

def view_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()
    if users:
        print("Kayıtlı kullanıcılar:")
        for user in users:
            print(f"ID: {user[0]}, Kullanıcı Adı: {user[1]}")
    else:
        print("Kayıtlı kullanıcı bulunmamaktadır.")

def main():
    conn = sqlite3.connect('users.db')
    create_table(conn)

    while True:
        print("\n1. Kullanıcı Ekle\n2. Kullanıcıları Görüntüle\n3. Çıkış")
        choice = input("Seçiminizi yapınız: ")

        if choice == '1':
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            add_user(conn, username, password)
        elif choice == '2':
            view_users(conn)
        elif choice == '3':
            print("Program sonlandırılıyor.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyiniz.")

    conn.close()

if __name__ == "__main__":
    main()
