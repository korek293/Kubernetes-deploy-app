array_ip = []
with open("text.txt", "r") as file:
    for line in file:
        ip = line.split(" ")[1]
        if ip not in array_ip:
            array_ip.append(ip)
output_ip = array_ip[-100:]

with open("output.txt", "w") as file1:
    for value in output_ip:
        file1.write(value + '\n')