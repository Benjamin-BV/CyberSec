#General security specifications for a password require: 
# At least 1 Uppercase
# At least 1 special character
# At least 1 Number
# At least 1 lowercase
# Minimum length of 8

#Minimum specs: Bq8#ozLv
#High specs: Io0w9eor;f'!@jaidsofzxcmMMDASIF>?193kdsfi

#How to code: First, randomly generate some ASCII inputs, maybe use some sort of tabling to get unique results on each run.

from random import *


charAmnt = 0;
def generate(char):
    #Setting flags to be global so changes in function apply to whole namespace, and are not erased after the fact
    global lowflag;
    global upflag; 
    global numflag;
    global specflag;
    
   
    #Generate a lowercase:
    if(char == 0):
        lowflag = True;
        return chr(SystemRandom().randint(97,122));
    #Generate an uppercase:
    if(char == 1):
        upflag = True;
        return chr(SystemRandom().randint(65,90));
    #Generate a number:
    if(char == 2):
        numflag = True;
        return str(SystemRandom().randint(0,9));
    #Generate a special char:     
    #Also should consider: [58,64], 
    #use an if conditional and set some RNG seeding for sysRandom 
    #so if RNG > .33, be this, if RNG > .66, be that, else be other or something similar to this 
    #consider invalid values and use those as selectors is another possibility
    if(char == 3):
        specflag = True;
        return chr(SystemRandom().randint(33, 47)) 
#^^^Make these in a reusable function so they can be called to again^^^
#Append characters from these outputs to a list
#Ask user for strength requirements (8,16,32 char passwords)
#Then print out the list, or store it to a specified folder (For extra brownie points)
def askPass():
    passReq = input("What strength do you need your password to be?(HIGH - 32 char, MED - 16 char, LOW - 8 char):\n");
    if(passReq.lower() == "high"):
        genPass(32);
    elif(passReq.lower() == "med" or passReq.lower() == "medium"):
        genPass(16)
    elif(passReq.lower() == "low"):
        genPass(8);
    else:
        print("Invalid input, please input either: HIGH, MED, LOW\n");
        askPass();

#Setting flag values
lowflag = False; upflag = False; numflag = False; specflag = False;
#Our flags that we use to determine when we have a character, making sure that we meet our char requirements
flags = [lowflag, upflag, numflag, specflag];
#Our password list, to be turned into a string 
pwd = [];

def genPass(chars):
    for i in range(0, chars):
        #Generate a random character, making sure we follow our specifications, and that we make sure that we do not miss a required target
            if(not all(flags) and i + (4 - sum (flags)) >= charAmnt):
                for j in range(0, 3):#failsafe to make sure each type of char is considered
                    if(flags[j] == False):
                        flags[j] = True;
                        pwd.append(generate(j))
                pwd.append(generate(randint(0,3)));
    print(''.join(pwd) + '\n');
    
def main():
    askPass();

main();