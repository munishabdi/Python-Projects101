
# Nested loops

for x in range(5):
    for y in range(3):
        # print("x:", x, "y:", y)
        print(f"({x}, {y})")

""" How the above code works...
    the inner loop will be executed 3 times 
    before the first iteration of the outer loop is executed
    in each iteration of the inner loop, 0 is printed 3 times 

"""
