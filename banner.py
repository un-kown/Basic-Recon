mport socket

ip = input("Enter IP/WebURL: ")
port = int(input("Enter Port number: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((ip, port))

    request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"
    s.send(request.encode())

    response = b""
    while True:
        data = s.recv(2048)
        if not data:
            break
        response += data

    response_text = response.decode(errors="ignore")

    print("\nBanner received:\n")

    # Extract ONLY headers
    headers = response_text.split("\r\n\r\n")[0]
    print(headers)

    s.close()

