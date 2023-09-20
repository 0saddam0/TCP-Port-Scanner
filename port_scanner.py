import argparse
import socket
import threading

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except (OSError, socket.error):
        return "NULL"

def port_scan(target_host, port):
    try:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        
        
        result = sock.connect_ex((target_host, port))
        if result == 0:
            service_name = get_service_name(port)
            print(f"open TCP {port} ({service_name}) ")
        
        
        sock.close()
    
    except socket.error:
        pass 
    except KeyboardInterrupt:
        pass  

def main():
    parser = argparse.ArgumentParser(description="FUCK NMAP")
    parser.add_argument("host", help="Target IP")
    
    args = parser.parse_args()
    
    target_host = args.host
    print ("Trash Nmap :)")
    print ("!! Only scannin for TCP ports !!")
    print(f"Running : {target_host}")
    
   
    for port in range(1, 65536):
        t = threading.Thread(target=port_scan, args=(target_host, port))
        t.start()

if __name__ == "__main__":
    main()
