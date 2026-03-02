str = "Kodnest"
# to extract a part of string
print(str[4])
print(str[2:3])
print(str[1:6])
print(str[-7:-4])

print("----step count positive------")
#step count positive
print(str[1:5:1])
print(str[1:5:2])
print(str[1::2])
print(str[::2])
print(str[::3])
# step count negative
print("----step count negative------")
print(str[-2::-1])
print(str[-2::-1])
#Reverse a string
print("-----Reverse a string-----")
print(str[::-1])
print(str[-6::-1])
print(str[-3:-6:-2])
print(str[::-3])


# Inbuilt String Methods – Single Program


s = "  kodNest Technologies 123  "


print("Original String:", s) #  kodNest Technologies 123  


# Case conversion methods
print("upper():", s.upper()) # KODNEST TECNOLOGIES 123
print("lower():", s.lower()) #   kodnest technologies 123  
print("capitalize():", s.capitalize()) #  kodnest technologies 123  
print("title():", s.title()) #  kodnest Technologies 123  
print("swapcase():", s.swapcase()) #kODNEST tECHNOLOGIES 123


# Searching & counting
print("find('Tech'):", s.find("Tech")) # 10
print("count('o'):", s.count("o")) #3


# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))
#  kodNest Technologies 2025  


# Start & End check
print("startswith('  kod'):", s.startswith("  kod")) #True
print("endswith('123  '):", s.endswith("123  ")) #True


# Split & Join
words = s.split() #["kodnest","Technologies,"123]
print("split():", words)
print("join():", "-".join(words)) #  kodNest - Technologies - 123  


# Strip spaces
print("strip():", s.strip()) #kodNest Technologies 123
print("lstrip():", s.lstrip())#kodNest Technologies 123  
print("rstrip():", s.rstrip())#  kodNest Technologies 123


# Checking methods
print("isalpha():", s.isalpha())#false
print("isdigit():", s.isdigit())#false
print("isalnum():", s.isalnum())#true


# Length
print("Length of string:", len(s)) #28