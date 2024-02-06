# The qualifies to take a loan of bank.
# The yearly salary should be minimnm 30000.0
# The customer should be 2 years on job

salary = 30000.0 
job = 2
Salary = float(input('Please enter your annual salary:'))
Job = float(input('Please enter how many years on job:'))
if Salary >= salary:
    if Job >= job:
        print('You qualify to take a loan!')
    else:
        print('your employed less than 2 years, you not reach the bank conditions!')
else:
    print('your salary less than $30000.0 you not reach the bank condition!')
    
