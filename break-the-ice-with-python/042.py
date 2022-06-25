# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

INPUT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Square_of_INPUT = list(map(lambda x: x**2, INPUT))
Square_of_EVEN_INPUT = list(filter(lambda x: x % 2 == 0, Square_of_INPUT))

print(Square_of_EVEN_INPUT)
