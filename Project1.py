#School Administration Program

import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)       #writer object

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Phone_Number", "Email_ID"])

        writer.writerow(info_list)

if __name__ == "__main__" :
    condition = True
    student_num = 1

    while(condition):
        student_info = input('Enter some student informations for student #{} in the following format(Name Age Phone Email):'.format(student_num))
        #print('Entered information:'+student_info)
        #split the informations Entered
        student_info_list = student_info.split(' ')
        #print('The Entered split up information is:'+ str(student_info_list))


        print("\nThe Entered information is -\nName: {}\nAge: {}\nPhone_Number: {}\nEmail ID: {}"
         .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input('Is the Entered informations correct? (yes/no):')
        if choice_check == 'yes':
            write_into_csv(student_info_list)           #Function call

            condition_check = input("Enter (yes/no) if you want to enter information for another student:")

            if condition_check == 'yes':
                condition = True
                student_num = student_num + 1
            elif condition_check == 'no':
                condition = False
        elif choice_check == 'no':
            print('\n Please Re-enter the correct informations!')
