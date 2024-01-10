
# Logical operators - (and, or, & not)
# "and" operator both conditions has to be true
# "Or" operator only one condition has to be true
# "Not" operator reverses the condition to fale if it were true

high_income = False
good_credit = True
student = True

if not student and (high_income or good_credit):
    print("Eligible")
else:
    print("Not eligible")

# if student is false, when we apply the not operator the condition is true
# and the else block will be executed
    