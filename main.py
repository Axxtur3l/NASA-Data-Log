file = open('NASA_access_log_Jul95')

ip_address = []

try:
    for line in file:
        ip_address.append(line.split(" ")[0])
except:
        print("uh-oh")

print(ip_address)