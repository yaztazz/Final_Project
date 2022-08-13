
import Grading_Rubric

def selection():     #selection process

    print('1- Total Points Earned')

    print('2- Average Points Earned')

    print('3- Letter Grade')


    try:



        option = int(input('Option number: '))
        while option < 1 or option > 3:
            option = int(input('Option number (1-3): '))

        return option

    except ValueError:
        print('Invalid data type')


def main():
    while True:

        try:


            option = selection()

            if (option == 1):
                homework = float(input('Homework points: '))
                test = float(input('Test points: '))
                bonus = float(input('Bonus points: ' ))
                print('Total Points Earned = ' ,Grading_Rubric.total_points(homework,test,bonus))
            

            elif (option == 2):
                homework = float(input('Homework points: '))
                test = float(input('Test points: '))
                bonus = float(input('Bonus points: ' ))
                print('Average Points Earned = ' ,Grading_Rubric.average_points(homework,test,bonus))


            elif (option == 3):
                homework = float(input('Homework points: '))
                test = float(input('Test points: '))
                bonus = float(input('Bonus points: ' ))
                print(Grading_Rubric.letter_grade(homework,test,bonus))

        except ValueError:
                print('Invalid data type')


        yes_no = input('Continue(y/n):').strip()

        while (True):

      
            if (yes_no != 'y'  and yes_no != 'Y' and yes_no != 'n' and yes_no != 'N'):
                yes_no = input('Continue(y/n): ').strip(' ').lower()

            else:
                break

        if (yes_no == 'y' or yes_no == 'Y'):

            continue

        else:
    
           
            print ('PROGRAM DONE')
            break


if __name__ == '__main__': 
    main()
        


            



