from AVLTree import *
import math
import random
tree = AVLTree()

def menu():  
    while True:
        print('----------MAIN MENU ------------')
        print('1. Read')
        print('2. Permute')
        print('3. Search')
        print('4. Height')
        print('5. Print')
        print('6. Quit\n')

        command = int(input("Enter a command: "))
            
        if command == 6:
            print('Program is now quitting!')
            break
        elif command == 1:
            fn = input("Enter the filename as $filename.txt ")
            print("Reading the file!")
            valid = False
            try:
                f = open(fn, 'r')
                valid = True
            except IOError:
                print("That file does not exist!")
            if valid:
                numbers(f, False)
                f.close()
        elif command == 2:
            num=int(input("Enter the number of elements you want: "))
            try:
                numbers(num,True)
            except ValueError:
                print("Please Enter a number")
        elif command== 3:
            num=int(input("Enter a number to be searched for: "))
            print("Searching and printing the route to the number " + str(num) + " in the Binary Search Tree")
            tree.search_print(num)
        elif command == 4:
            tree.max_height()
        elif command == 5:
            tree.print_in_order()
        else:
            print("Invalid Input. Try again.\n")

def numbers(filename, random):
 
    number_list = []
    if not random:
        tree.reset()
        # Writing all numbers into number_list
        for _ in filename:
            number_list += _.split()
        # Inserting the numbers into the BST
        for i in number_list:
            tree.insert(int(i))
        print("All numbers have been inserted")
    else:
        tree.reset()
        # Writing all numbers into number_list
        # Inserting the numbers randomly into the BST
        for i in range(1,filename+1):
            number_list.append(i)
        for i in permute_array(number_list):
            tree.insert(i)
        print("All numbers have been inserted")
    
    print("Printing inorder: ")
    tree.print_in_order()

def permute_array(alist):
    n = len(alist) 
    for i in range(0, n-1): 
        j = random.randint(i, n-1) 
        swap(alist, i, j) 
    return alist 

def swap(alist, i, j):
    tmp = alist[i] 
    alist[i] = alist[j] 
    alist[j] = tmp 


if __name__ == "__main__":
    menu()
