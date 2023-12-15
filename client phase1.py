##                Network Project 
##           1402-1403  First semester 
##            Saeed Norouzi 982013210 
##            Hamid Akhavan 982023002 
## 
 
 

 
 
import socket 

 
print("SAEED NOROUZI\n") 
print("HAMID AKHAVAN\n") 

            ############################## 
                   #### phase 1 ## 
            ############################## 
 
                     ## part 1 ## 
 
 
def check_server_status(server_ip, port): 
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(5) 
        result = sock.connect_ex((server_ip, port)) 
        if result == 0: 
            print("The server is online.\n") 
            return "The server is online." 
        else: 
            print("The server is offline.\n") 
            return "The server is offline." 
         
    except socket.error as e: 
        return "An error occurred while checking the server status: {}".format(e) 
     
    finally: 
        sock.close() 
 
 
            ############################## 
                   #### phase 1 ## 
            ############################## 
 
                     ## part 2 ## 
 
# Define the server IPs 
ports=[20,21,22,25,53,80,443,123] 
 
def check_port(ip, port): 
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(3) 
        con=sock.connect_ex((ip, port)) 
        result=socket.getservbyport(port) 
        print(port,result,"\n") 
        sock.close() 
        return con==0,port 
    except socket.error as e: 
        return "An error occurred while checking the server PORT: {}".format(e) 
    finally: 
        sock.close()   
 
            ############################## 
                   #### phase 1 ## 
            ############################## 
 
                     ## part 3 ## 
 
def GET_method(ip,port,user_id): 
      try: 
            sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            sock.connect((ip,port)) 
            req=b"GET "+user_id.encode() 
            sock.sendall(req) 
            response = sock.recv(4096) 
      ##      print(response.decode()) 
            sock.close() 
            return response.decode() 
      except socket.error as e: 
            return "Error: {}".format(e) 
 
 
def POST_method(ip,port,user_name,user_age): 
      try: 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            sock.connect((ip, port)) 
            request = b"POST "+user_name.encode()+b" "+user_age.encode() 
            sock.sendall(request) 
            response = sock.recv(4096) 
            print(response.decode()) 
            sock.close() 
            return response.decode() 
      except socket.error as e: 
        return "Error: {}".format(e) 
 
 
                     ############################## 
################################ menu ################################## 
                     ############################## 
def menu(): 
      port = 8080 
      print("Choose one of the options below") 
      choise=input("G:GET\nP:POST\nPORTS:Server Ports Check\nC:Server Connection Check\n") 
       
      if choise=="G": 
            server_ip = input("Enter your server IP\n")  
            id=input("Enter your user id\n") 
            print(GET_method(server_ip,port,id)+"\n") 
             
      elif choise=="P": 
            server_ip = input("Enter your server IP\n")  
            name=input("Enter your username\n") 
            age=input("Enter your user age\n") 
            print(POST_method(server_ip,port,name,age)) 
             
      elif choise=="PORTS" : 
            server_ip = input("Enter your server IP\n")  
            status = check_server_status(server_ip, port) 
            if status == "The server is online." : 
                  for port in ports:
                      if check_port(server_ip, port): 
                          print(f"Port {port} is open") 
 
      elif choise=="C": 
            server_ip = input("Enter your server IP\n")  
            status = check_server_status(server_ip, port) 
      else : 
          print("Please choose through the options(G,P,PORTS,C)") 
 
while True : 
      menu()
