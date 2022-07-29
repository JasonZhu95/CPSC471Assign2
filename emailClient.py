import base64
import socket
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, 587))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')

command = 'STARTTLS\r\n'.encode()
clientSocket.send(command)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] !='220':
    print('220 reply not received from server')

clientSocket = ssl.wrap_socket(clientSocket)

# Email and Password
email = (base64.b64encode('throwawaycpsc471@gmail.com'.encode()) + ('\r\n').encode())
password = (base64.b64encode('eqvwuqlhylbaluii'.encode()) + ('\r\n').encode())

# Authenticate
clientSocket.send('AUTH LOGIN \r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '334':
    print('334 reply not received from server')

clientSocket.send(email)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '334':
    print('334 reply not received from server')

clientSocket.send(password)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '235':
    print('235 reply not received from server')

# Send MAIL FROM command and print server response.
clientSocket.send("MAIL FROM: <throwawaycpsc471@gmail.com>\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '250':
    print('250 reply not received from server')

# Send RCPT TO command and print server response.
clientSocket.send("RCPT TO: <throwawaycpsc471@gmail.com>\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send DATA command and print server response.
clientSocket.send("DATA\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send message data.
clientSocket.send(("Subject: This is an SMTP Email Client Test \r\n").encode())
clientSocket.send(("To: throwawaycpsc471@gmail.com \r\n").encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

clientSocket.close()
