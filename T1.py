import socket

host = '172.17.8.83'
port = 50038
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

print 'waiting for clients to connect...'
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data == '<Salamon alaikom va rahmatollahe va barakatoh!>':
        print '#client connected'
        client.send('<Alaikom ossalam>')
        break

client.send('<[1,0,1,1]>')
data = client.recv(size)
if (data == '<UP>'):
    print 'ok!'
    print data
    client.send('<Halle!>')

else:
    print data
    print 'invalid'
    client.send('<Invalid Move!>')
