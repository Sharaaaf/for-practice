# movie = []
# movie.append(input("Give me 1st choice: "))
# movie.append(input("Give me 2nd choice: "))
# movie.append(input("Give me 3rd choice: "))

# print(movie)

movie_list = input("Give me responses: ").split()
print (movie_list)

# list = [1,2,5,2,3]

# list = (input("Write your thing: "))

# b = list.copy()
# b.reverse()

# if (list == b) :
#     print("Palindrome")
# else :
#     print("Not palindrome")

my_list = [int(x) for x in input().split()]
b = my_list.copy()
c = b.reverse

if (c == my_list):
    print("Palindrome")
else:
    print("Not Palindrome")
