inputs=list()
for i in range(10):
    try:
        num=int(input(f"Enter integer {i + 1}: "))
        inputs.append(num)
    except ValueError:
        print("Invalid input")
sum=sum(inputs)
print("sum of the list : %d",sum)
maximum=max(inputs)
print("Maximum integer: %d",maximum)
minimum=min(inputs)
print("Minimum integer: %d",minimum)
