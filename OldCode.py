# Sub Programs
def ErrorCode(code):
    if(code == 0):
        print("Username must be at least 5 characters long")
    if(code == 1):
        print("Username must only contain alphanumeric characters")
    if(code == 2):
        print("Password must be at least 8 characters long")
    if(code == 3):
        print("Password must contain an uppercase and a lowercase character")
    if(code == 4):
        print("Password must contain a digit")
    if(code == 5):
        print("Email must contain '@' symbol")
    if(code == 6):
        print("Phone number must be 11 digits long")

def VerifyCode(code):
    if(code == 0):
        print("Username Successfully Added")
    if(code == 1):
        print("Password Successfully Added")
    if(code == 2):
        print("Email Successfully Added")

def CreateUserName():
    value = input("Enter you username: ")
    if(len(value) >= 5):
        if(value.isalnum()):
            VerifyCode(0)
            return value, 0b0000_0001
        else:
            ErrorCode(1)
    else:
        ErrorCode(0)
    return "", 0b0000_0000

def CreatePassword():
    value = input("Enter you password: ")
    if(len(value) >= 8):
        if(value.lower() != value and value.upper() != value):
            containsDigit = ContainsDigit(value)
            if(containsDigit):
                VerifyCode(1)
                return value, 0b0000_0010
            else:
                ErrorCode(4)
        else:
            ErrorCode(3)
    else:
        ErrorCode(2)
    return "", 0b0000_0000

def AddEmail():
    value = input("What is your email: ")
    if(ContainsCharacter(value, "@")):
        VerifyCode(2)
        return value, 0b0000_0100
    else:
        ErrorCode(5)
    return "", 0b0000_0000

def AddPhoneNumber():
    value = input("What is your phone number: ")
    if(len(value) == 11 and value.isdigit):
        return value, 0b0000_1000
    else:
        ErrorCode(6)
    return "", 0b0000_0000

def AddDateOfBirth():
    value = input("What is your date of birth. Enter in format DD MM YYYY: ")
    userAge = CalculateAge(value)
    if(userAge >= 18 and userAge <= 100):
        return value, userAge, 0b0001_0000
    return "", 0, 0b0000_0000

def AddCreditCard():
    pass


def ContainsDigit(value):
    containsDigit = False
    for x in range(len(value)):
        if(value[x].isdigit()):
            containsDigit = True
    return containsDigit

def ContainsCharacter(value, char):
    containsChar = False
    for x in range(len(value)):
        if(value[x] == char):
            containsChar = True
    return containsChar

def CheckIfValidFormat(value):
    valid = True
    valid = len(value) == 10
    if(valid == False):
        return False
    
    if(value[0:1].isnumeric() and value[3:4].isnumeric() and value[6:9].isnumeric()):
        valid = True
    else:
        return False
    
    if(value[2] == " " and value[5] == " "):
        valid = True
    else:
        return False
    
    return valid

def CalculateAge(value):
    currentD = 20
    currentM = 9
    currentY = 2024

    parts = value.split(" ")
    if(CheckIfValidFormat(value)):
        userD = int(parts[0])
        userM = int(parts[1])
        userY = int(parts[2])
        userAge = (currentY - userY) - ((userM - currentM) / 12) - ((userD - currentD) / 365)
        return userAge

    return 0

    

# Main Code
authentication = 0b0000_0000
username    = ""
password    = ""
email       = ""
phoneNumber = ""
cardNumber  = ""
dateOfBirth = ""
age         = 0
values = ()

while (authentication < 1):
    values = CreateUserName()
    username = values[0]
    authentication += values[1]

while (authentication < 2):
    values = CreatePassword()
    password = values[0]
    authentication += values[1]

while (authentication < 4):
    values = AddEmail()
    email = values[0]
    authentication += values[1]

while (authentication < 8):
    values = AddPhoneNumber()
    phoneNumber = values[0]
    authentication += values[1]

while (authentication < 16):
    values = AddDateOfBirth()
    dateOfBirth = values[0]
    age = values[1]
    authentication += values[2]

#print(dateOfBirth)
#print(age)
#print(authentication)
