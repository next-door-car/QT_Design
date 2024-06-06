import socket
import time
import select


PORT = 1881
BUFFER_SIZE = 1024
arrea = ["00000001", "00000010", "00000100", "00001000", "00010000"]

def main():
    i=0
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", PORT))
    server_socket.listen(1)

    print("Get a connect!")
    client_socket, client_address = server_socket.accept()
    print("Client connected:", client_address)
    print("IP:", client_address[0])

    while True:
        client_socket.send(arrea[i].encode())
        print(f"Sent: {arrea[i]}")
        i=i+1
        if i == 5:
            i = 0
        time.sleep(3)
        ready = select.select([client_socket], [], [], 1)  # 设置1秒超时
        if ready[0]:
            data = client_socket.recv(BUFFER_SIZE).decode()
            if data == "close":
                client_socket.send("close".encode())
                print("Server close")
                break
            else:
                print("Received:", data)
        else:
            print("No data received within 1 second. Exiting...")
            

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()