#Write your code below this row 👇
total = 0
for number in range(1, 101):
    #should have used an if loop and added them at the end
    even = int(number % 2 == 0)
    print(even)


total2 = 0
#should start number at two if wnated even numbers
for number in range(2, 101, 2):
    total2 += number
print(total)