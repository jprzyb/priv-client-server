import socket


def main():
    # Tworzenie gniazda klienta
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Pobieranie adresu IP serwera i portu
    server_ip = input("Podaj adres IP serwera: ")
    port = 12345

    # Łączenie z serwerem
    client_socket.connect((server_ip, port))

    # Wysyłanie nazwy pliku do serwera
    file_name = input("Podaj nazwę pliku do wysłania: ")
    client_socket.send(file_name.encode())

    # Otwieranie pliku do wysłania
    with open(file_name, 'rb') as file:
        print("Wysyłanie pliku...")
        # Wysyłanie danych pliku do serwera
        for data in file:
            client_socket.send(data)
        print("Plik wysłany.")

    # Zamykanie połączenia z serwerem
    client_socket.close()


if __name__ == "__main__":
    main()
