# trial project

# -Shuffles

# even: rotate clockwise
# odd: rotate counterclockwise
# prime: reverse dots
# next prime: reset all changes
# duplicate as last: reverse triangles with adjecent squares

# active shuffles
shuffle = []
lastShuffle = 0
lastPrime = 0

# Shuffles-

#print(len(myList))

# default box values
dBox1 = {"D", "A", "V", "U", "Z", "E", "S", "C", "G"}
dBox2 = {"K", "I", "R", "L"}
dBox3 = {"B", "N", "F", "X", "O", "Y", "Q", "J", "P"}
dBox4 = {"M", "T", "H", "W"}

#current box values
box1 = ["D", "A", "V", "U", "Z", "E", "S", "C", "G"]
box2 = ["K", "I", "R", "L"]
box3 = ["B", "N", "F", "X", "O", "Y", "Q", "J", "P"]
box4 = ["M", "T", "H", "W"]
boxes = [box1, box2, box3, box4]

#post-shuffle box sample
def current_box():
    print(box1[0] + " " + box1[1] + " " + box1[2] + "    " +
          box2[0] + "    " +
          box3[0] + " " + box3[1] + " " + box3[2] + "    " +
          box4[0] + "\n" +
          
          box1[3] + " " + box1[4] + " " + box1[5] + "  " +
          box2[1] + "   " + box2[2] + "  " +
          box3[3] + " " + box3[4] + " " + box3[5] + "  " +
          box4[1] + "   " + box4[2] + "  \n" +
          
          box1[6] + " " + box1[7] + " " + box1[8] + "    " +
          box2[3] + "    " +
          box3[6] + " " + box3[7] + " " + box3[8] + "    " +
          box4[3] + "\n"       
        )

    
# prompts and prints the code
def string_to_int():
    string = ""
    code = list(map(str, interpret_string()))
    for x in range(len(code)):
        string =(string + code[x] + "  ")
    print(string)

    
# converts the string into numbers    
def interpret_string():
    text = input("enter a string! ").upper()
    encoded = []
    print(text)
    code = [x for x in text]
    for x in range(len(code)): 
        if code[x] == " ":
           encoded.append("_")
        else:
            for i in range(len(boxes)):
                num = (box_check(code[x], i))
                if num is None:
                    num = 0
                else:    
                    encoded.append(num)
    return(encoded)
                    
           
# checks which box and what index the character is                
def box_check(x, i):
    codeLetter = x
    boxNumber = i
    if codeLetter in boxes[i]:
        number = (boxes[i].index(codeLetter))
        return(box_number(boxNumber, number))
        

# Fixes the box number
def box_number(boxNumber, number):
    if boxNumber > 0:
        number += 9
    if boxNumber > 1:
        number += 4
    if boxNumber > 2:
        number += 9   
    return(number)

# prompts and deciphers code
def int_to_string():
    message = interpret_int()

# prompts a code to begin 
def interpret_int():
    text = input("enter a code seperated by double spaces: ")
    digits = [x for x in text]
    #print(digits)
    print(scan_digits(digits))

# combines message into proper numbers and lists
def scan_digits(code):
    current = ""
    skip = 0
    send = []
    for x in range(len(code)):
        if code[x] == " ":
            skip = skip + 1
            if skip == 2:
                send.append(current)
                send.append("_")
                skip = 0
                current = ""
        else:
            current += code[x]

    return(send)

# 1  12  15  11  5  0


def repeat():
    #current_box()
    string_to_int()
    #int_to_string()
    repeat()
    
repeat()

