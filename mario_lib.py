import os
import csv

def read_and_combine(bodies_file, char_file):
    """
    read from the bodies file and the char file
    (CSV) and then iterate thru both of them (nested)
    and to print out all the combinations
    """
    bodies_dict={}
    char_dict={}
    combined_dict={}
    with open(bodies_file, 'r') as f_bodies, open(char_file, 'r') as f_chars:
        f_bodies.readline()
        read_bodies= csv.reader(f_bodies)
        for row in read_bodies:
            body=str(row[0])
            type=str(row[1])
            speed=float(row[2])
            acceleration=float(row[3])
            weight=float(row[4])
            handling=float(row[5])
            traction=float(row[6])
            mini_turbo=float(row[7])
            bodies_dict[body]=type, speed, acceleration, weight, handling, traction, mini_turbo
        f_chars.readline()
        read_chars= csv.reader(f_chars)
        for row in read_chars:
            char=str(row[0])
            speed=float(row[1])
            acceleration=float(row[2])
            weight=float(row[3])
            handling=float(row[4])
            traction=float(row[5])
            mini_turbo=float(row[6])
            char_dict[char]=speed, acceleration, weight, handling, traction, mini_turbo
        print('Bodies dict')
        print(bodies_dict)
        print('Char dict')
        print(char_dict)
    key=0
    for body in bodies_dict:
        for char in char_dict:
            combined_speed=0
            combined_acceleration=1
            combined_weight=2
            combined_handling=3
            combined_traction=4
            combined_mini_turbo=5
            combined_dict[key]=body, bodies_dict[body], char
            key=+1

    print(combined_dict)
    pass

def best_speed(bodies_file, char_file):
    """
    read from bodies and char files
    iterate thru them all and get the speed
    sum the speed for the character and the body
    print out the character/body combo that has the highest
    speed.  And print out the highest (total) speed.
    """
    pass

def best_acceleration(bodies_file, char_file):
    """
    """
    pass


# TODO refactor and consider if there's a better way than passing in the
# filename each time
# with open(my_dir + '/' + filename, 'r')  as f:
    # read_csv= csv.reader(f)
    # for row in read_csv:
    #     key=int(row[0])
    #     value=(row[1]).lstrip()
    #
    #     my_dict[key]=value
