if check_port(server_ip, port): 
                          print(f"Port {port} is open") 
 
      elif choise=="C": 
            server_ip = input("Enter your server IP\n")  
            status = check_server_status(server_ip, port) 
      else : 
          print(colored("Please choose through the options(G,P,PORTS,C)") 
 
while True : 
      menu()
