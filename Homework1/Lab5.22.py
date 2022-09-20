# JenniferChu
# 1873159

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

total1 = 0
total2 = 0

service1 = input("Select first service:\n")
if service1 == "Oil change":
    total1 = 35
elif service1 == "Tire rotation":
    total1 = 19
elif service1 == "Car wash":
    total1 = 7
elif service1 == "Car wax":
    total1 = 12
elif service1 == "-":
    service1 = "No service"
    total1 = 0

service2 = input("Select second service:\n")
if service2 == "Oil change":
    total2 = 35
elif service2 == "Tire rotation":
    total2 = 19
elif service2 == "Car wash":
    total2 = 7
elif service2 == "Car wax":
    total2 = 12
elif service2 == "-":
    service2 = "No service"
    total2 = 0

print("\nDavy's auto shop invoice\n")
if total1>0:
    print("Service 1:", service1 + ",", f'${total1:.0f}')
else:
    print("Service 1:", service1)
if total2>0:
    print("Service 2:", service2 + ",", f'${total2:.0f}')
else:
    print("Service 2:", service2)

total = total1 + total2
print("\nTotal:", f'${total:.0f}')