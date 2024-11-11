import socket


def main():
    # Tworzenie gniazda serwera
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Pobieranie adresu IP i portu serwera
    host = socket.gethostname()
    port = 12345

    # Przypisanie adresu IP i portu do gniazda serwera
    server_socket.bind((host, port))

    # Nasłuchiwanie na połączenia przychodzące
    server_socket.listen(5)

    print("Serwer nasłuchuje: ", host, ":", port)

    while True:
        # Akceptowanie połączenia od klienta
        client_socket, addr = server_socket.accept()
        print('Połączono z', addr)

        # Odbieranie nazwy pliku od klienta
        file_name = client_socket.recv(1024).decode()
        print("Odebrano nazwę pliku:", file_name)

        # Otwieranie pliku do zapisu
        with open(file_name, 'wb') as file:
            print("Odbieranie pliku...")
            # Odbieranie danych pliku od klienta i zapisywanie ich do pliku na serwerze
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
            print("Plik odebrany i zapisany.")

        # Zamykanie połączenia z klientem
        client_socket.close()


if __name__ == "__main__":
    main()
