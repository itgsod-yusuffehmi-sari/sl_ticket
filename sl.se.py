def fares(age, student=False, senior=False):
    if student or senior:
        return 'halv'
    else:
        if age < 20 or age>65:
            return 'halv'
        else:
            return 'hel'


# test cases
print 'child 10', fares(10)
print 'senior 15',fares(15,senior=True)
print 'student 15',fares(15,student=True)
print 'adult 30', fares(30)

print 'hej'