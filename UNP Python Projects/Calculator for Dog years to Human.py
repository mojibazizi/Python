import traceback
dog_1 = 15
dog_2 = 12
dog_3 = 9.3
dog_4 = 8
dog_5 = 7.2
dog_old = 7    

        # Get dog age
age = input("Input dog years: ")
6

try:
        # Cast to float
        age = float(age)

        # If user enters letter
        # Otherwise, calculate dog's age in human years
    
        # your code here
        if age<0:
                print("Negative Input") 

        elif (age <= 1):
                h_age = dog_1*age

        elif (age > 1 and age <= 2):
                h_age = dog_2*age

        elif (age > 2 and age <= 3):
                h_age = dog_3*age
        elif (age > 3 and age <= 4):
                h_age = dog_4*age
        elif (age > 4 and age <= 5):
                h_age = dog_5*age
        elif (age > 5):

                # if input is 8 => ((8-5)*7+5*7.2)
                # output is h_age
                # 8 is age 
                # -5 is operation
                # 7 is dog_old
                # 5 is opration
                # 7.2 dog_5
                # BEDMAS 

                h_age = (age - 5) * dog_old + (5 * dog_5) 

        

        try:
                print('The given dog age {0:.2f} is {1:.2f} in human years'.format(age,h_age))
        except:
                pass
    
except:
        print(age, "is an invalid age.")
        # print(traceback.format_exc())
        





        

      

