import os
from time import sleep


# MAIN FUNCTION - AT START, IT DECIDES WETHER CONTINUE TO PING THE DEFINED HOST OR TO RECONNECT


def ping():
    listener = os.system("ping -n 1 192.168.0.52")
    sleep(3)
    listener = os.system("ping -n 1 192.168.0.52")
    sleep(3)
    listener = os.system("ping -n 1 192.168.0.52")
    sleep(3)

    while listener == 0:
         continue_ping()

    while listener == 1:
         conditional()


# IF PING IT´S WORKING FINE, MAIN FUNCTION LEADS TO THIS FUNCTION, WHERE IT GOING TO CONTINUE PINGUING THE HOST UNTIL PING FAILS.


def continue_ping():
    listener = os.system("ping -n 1 192.168.0.52")
    while listener == 0:
        os.system("ping -n 1 192.168.0.52")
        sleep(3)
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        print('. . . : : : O N L I N E : : : . . . . . . : : : O N L I N E : : : . . .')
        os.system("color 2f")
        sleep(2)
        listener = os.system("ping -n 1 192.168.0.52")
        sleep(2)
        if listener == 1:
            ping()


# CONDITIONAL FUNCTION


def conditional():
    listener_conditional = os.system("ping -n 1 10.88.99.28")
    if listener_conditional == 1:
        os.system("color 4f")
        sleep(3)
        os.system("rasdial previus_vpn user password123")
        sleep(3)
        os.system("color 6f")
        sleep(3)
        print("VPN OK")
        print("VPN OK")
        print("VPN OK")
        print("VPN OK")
        print("VPN OK")
        print("VPN OK")
        print("VPN OK")
        print("VPN OK")
        sleep(2)
        listener_conditional = os.system("ping -n 1 10.88.99.28")
        sleep(2)
        listener_conditional = os.system("ping -n 1 10.88.99.28")
        sleep(2)
    else:
        reconnect()


# IF PING FAILS, MAIN FUNCTION ITS GOING TO DECIDE TO USE THIS FUNCTION TO SEND THE NEEDED PARAMETERS TO FORTICLIENT TO RECONNECT. THIS IS HAPPENING TROUGH THE EXECUTION OF 'VPNRECONNECT.BAT'.


def reconnect():
    listener = os.system("ping -n 1 192.168.0.52")
    while listener == 1:
        os.system("color 6f")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        print(". . . : : : R E C O N E C T A N D O : : : . : : : R E C O N E C T A N D O : : : . . .")
        sleep(7)
        os.system("start vpnconnect.bat")
        sleep(30)
        listener = os.system("ping -n 1 192.168.0.52")
        sleep(2)
        if listener == 0:
            ping()



if __name__ == '__main__':
    ping()
