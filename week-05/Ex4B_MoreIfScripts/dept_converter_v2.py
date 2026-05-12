#  Once your script is working, rewrite it using a 
# match/case statement instead of if/elif/else

dep_code = int(input('What is your department code: '))

match dep_code:
    case 1:
         print('You are in the Marketing Department')
    case 5:
          print('You are in the Human Resources Department')
    case 10:
          print('You are in the Accounting Department')
    case 12:
          print('You are in the Legal Department')
    case 18:
          print('You are in the IT Department')
    case 20:
            print('You are in the Customer Relations Department')