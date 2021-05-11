#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input
ipcchk = ipchk.split(".")

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif (len(ipcchk)) != 4:
   print("Not an IP Address")
elif (len(ipcchk)) == 4:
   print("Is an IP Address", ipchk)
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

