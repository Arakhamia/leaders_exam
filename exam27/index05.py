# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

def replace(x):
    y = []
    for i in x:
        # if i[0] == i[0].upper():
        #     y.append(f"{i}_")
        # else:
        #     y.append(f"_{i}")
        y.append(i)

    for i in y:
        if i[0] == i[0].upper():
            y.append(f"{i}_")
        elif i == i.upper():
            y.append(f"_{i}")
        else:
            y.append(i)
    return y
print(replace("PascalCase"))