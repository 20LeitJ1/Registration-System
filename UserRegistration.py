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

def CalculateAge(value):
    currentDate = "19 09 2024"

def DOBformatChecker(value):
    pass

# Main Code
authentication = 0b0000_0000
username    = ""
password    = ""
email       = ""
phoneNumber = ""
cardNumber  = ""
dateOfBirth = ""
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

print(phoneNumber)
print(authentication)
