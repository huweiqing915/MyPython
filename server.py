import socket, threading,time

def tcplink(sock, addr):
	print 'accept new connection from %s:%s' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send("Hello, %s!" %data)
	sock.close()
	print 'connection from %s:%s closed' % addr 

print 'Create server socket...'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Done'
print 'Bind'
s.bind(('127.0.0.1', 9999))
print 'Bind Done!'
s.listen(5)
print 'Waiting for connection...'

while True:
	sock, addr = s.accept()
	t = threading.Thread(target = tcplink, args=(sock,addr))
	t.start()

