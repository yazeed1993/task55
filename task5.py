user_name = input('Your Name is : ')
user_age = input('Your Age is : ')
user_street = input('Your Street is : ')
user_city = input('Your City is : ')
user_country = input('Your Country is : ')
print(' "Name: ' + user_name + '" ')
print(' "Age: ' + user_age + '" ')
print(' "Address: ' + user_street + ', ' + user_city + ', ' + user_country + '" ')
new_age = int(user_age) - 5
print(' "hello' + ' {' + user_name + '}' + ' Your Age Is '+ str(new_age) +\
      ' Your Address Is ' + user_street + ', ' + user_city + ', ' + user_country + '." ')
print(type (user_name),type(user_age), type(user_street) , type(user_city) , type(user_country))
print(' "hello' + " '"  + user_name + "', How Are You? \ " +\
      ' """ Your Age Is "'+ str(new_age) +\
      '"" + And Your country Is '  + user_country)
msg = f'''
 "hello '{user_name}', How Are You? \
   """ Your Age Is "{str(new_age)} "" + And
      Your country Is {user_city}'''
print(msg)
name = 'Doaa Reem'
name1 = 'DoAa'
name2 = 'Re em'
name3 = 'Reem'
print(name.capitalize())
print(name.strip('Doaa R'))
print(name.strip(' Re,em'))
print(name1.strip('Do'),name2.strip('em'))
print(name3[::-1])
print(name[0:4:2],name[4:7])
name = "$&$&Mohammed$&$&"
print(name.strip('$&'))
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7','love'))
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(str(num1).zfill(5))
print(str(num2).zfill(5))
print(str(num3).zfill(5))
print(str(num4).zfill(5))
print(str(num5).zfill(5))
print(str(num6).zfill(5))
first_name = "Hadeel"
print(f'''***********{first_name}
***********{first_name}***********
{first_name}***********
''')
name_one = "HaLA"
name_two = "shaHD"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())