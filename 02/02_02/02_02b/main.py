''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
Going to be developing a few different containers
'''
student_pet_count_list = [0,1,0,2,1,1,4,0,0,0,3,2,1,3,0,2,2,4]

ITEM_AT_INDEX_THREE =student_pet_count_list[3]
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]
print(ITEM_AT_INDEX_THREE)

NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
  
