import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                nickname = input("Bir kullanıcı adı girin: ")
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Sunucu bağlantısı kesildi.')
            client.close()
            break

def write():
    while True:
        message = input('')
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
