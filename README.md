# Sockets
This Python code is an example of communication between a client and a server, allowing the client to request specific currency quote information and the server to send that information back to the client.

The client code begins by importing the socket library to create a connection to the server. It obtains the host name and port number to connect to the server. It then creates a TCP socket (SOCK_STREAM) and connects to the server.

The client sends a message to the server requesting a specific currency quote, and the server responds with the requested currency quote. The client checks if the message sent is '0' (to quit) or a valid number corresponding to the currency quote it wants to receive. It then receives the server's response and displays the current currency quote to the user.

The server code imports the socket, requests, and json libraries. It then defines a menu of currency quote options and creates variables to store the currency quote information obtained through the API.

The server waits for a connection from a client and sends the currency quote options menu to the client. It receives the client's choice and checks if the message received is '0' (to quit) or a valid number corresponding to the currency quote the client wants to receive. It then sends the current currency quote corresponding to the client.

In summary, this Python code is an example of client-server communication using TCP sockets, allowing a client to request specific currency quote information and a server to send that information back to the client. The currency quote information is obtained through a third-party API.











