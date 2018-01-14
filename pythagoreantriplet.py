"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# http://www.friesian.com/pythag.htm

Triplet = [0, 0, 0]
TripletFound = False

for Q in range(1, 15):
    for P in range(Q, 15):

        if Q % 2 and P % 2:
            break

        Triplet[0] = 2 * P * Q
        Triplet[1] = P ** 2 - Q ** 2
        Triplet[2] = P ** 2 + Q ** 2

        TripletSum = 0
        for i in Triplet:
            TripletSum += i

        if TripletSum == 100:
            TripletFound = True
            break

    if TripletFound:
        break

TripletProduct = 1

for i in Triplet:
    TripletProduct *= i

print(TripletProduct)
