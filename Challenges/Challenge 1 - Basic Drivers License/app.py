# Challenge 1 - Basic Drivers License Script
# Requirements:
#   - Utilize variables to store string literals pertaining to each metric on a Drivers License
#   - Use print function calls to print all data to the console
#   - The console should print exactly like the example
# 
# Example:
#       State: NY
#       Class: D
#       License Number: 0123456
#       Date Issued: 03/02/2023
#       Date Expires: 03/02/2028
#       Name: Tony Stark
#       Date of Birth: 05/29/1970
#       Hair Color: Brown
#       Eye Color: Blue
#       Height: 67 inches
#       Weight: 154 lbs
#       Gender: M
#       Address: 200 Park Avenue New York, NY 10166
# 

# Insert Variable Data Here
residentState = 'NY'
licenseClass = 'D'
licenseNumber = '0123456'
dateIssued = '03/02/2023'
dateExpires = '03/02/2028'
firstName = 'Tony'
lastName = 'Stark'
dateOfBirth = '05/29/1970'
height = 67
weight = 154
gender = 'M'
eyeColor = 'Blue'
hairColor = 'Brown'
residenceHouseNumber = '200'
residenceStreet = 'Park Avenue'
residenceCity = 'New York'
residenceZipCode = 10166
blankspace = ' '

# Main Method - Code out the rest of the main method to print all data like the given example
# Tip: Use the str() method to cast integers to strings https://tinyurl.com/python-string-function
if __name__ == '__main__':
    print('State: ' + residentState)
    print('Class: ' + licenseClass)
    print('License Number: ' + licenseNumber)
    print('Date Issued: ' + dateIssued)
    print('Date Expires: ' + dateExpires)
    print('Name: ' + firstName + blankspace + lastName)
    print('Date of Birth: ' + dateOfBirth)
    print('Hair Color: ' + hairColor)
    print('Eye Color: ' + eyeColor)
    print('Height: ' + str(height) + ' inches')
    print('Weight: ' + str(weight) + ' lbs')
    print('Gender: ' + gender)
    print('Address: ' + residenceHouseNumber + ' ' + residenceStreet + ' ' + residenceCity + ', ' + residentState + ' ' + str(residenceZipCode))
