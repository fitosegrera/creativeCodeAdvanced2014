import socket   
import sys  
import struct
import time

class socketClient:
	def send(self, data):
		global message
		message = data

	def connect(self, host, port, message):
		#create an INET, STREAMing socket
		try:
		    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
		    print 'Failed to create socket'
		    sys.exit()

		print 'Socket Created'

		try:
		    remote_ip = socket.gethostbyname( host )
		    s.connect((host, port))

		except socket.gaierror:
		    print 'Hostname could not be resolved. Exiting'
		    sys.exit()

		print 'Socket Connected to ' + host + ' on ip ' + remote_ip
		
		try :
		    #Set the whole string
		    while True:
		        s.send(message)
		        print 'Message sent successfully'
		        time.sleep(1)
		        print 'Sending...'
		except socket.error:
		    #Send failed
		    print 'Send failed'
		    sys.exit()

		def recv_timeout(the_socket,timeout=2):
		    #make socket non blocking
		    the_socket.setblocking(0)

		    #total data partwise in an array
		    total_data=[];
		    data='';

		    #beginning time
		    begin=time.time()
		    while 1:
		        #if you got some data, then break after timeout
		        if total_data and time.time()-begin > timeout:
		            break

		        #if you got no data at all, wait a little longer, twice the timeout
		        elif time.time()-begin > timeout*2:
		            break

		        #recv something
		        try:
		            data = the_socket.recv(8192)
		            if data:
		                total_data.append(data)
		                #change the beginning time for measurement
		                begin=time.time()
		            else:
		                #sleep for sometime to indicate a gap
		                time.sleep(0.1)
		        except:
		            pass

		    #join all parts to make final string
		    return ''.join(total_data)

		#get reply and print
		print recv_timeout(s)

		s.close()