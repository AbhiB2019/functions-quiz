	
def has_teen(a, b, c):
	if 13 <= a <= 19 or 13 <= b <= 19 or 13 <= c <= 19:
		return True
	else:
		return False
print has_teen(13, 123, 132)
print has_teen(13, 123, 13)
print has_teen(13, 13, 5)
print has_teen(13, 13, 15)
print has_teen(11, 11, 11)

def not_string(str):
	if str[0:3] == "not":
		return str + "not"
	return "not" + str
print not_string("aasdas")
print not_string("not aasdas")
print not_string("not aasdas not")

def icy_hot(a, b):
	if a > 100 and b < 0:
		return True
	if a < 0 and b > 100:
		return True
	else:
		return False
print icy_hot(100, 0)
print icy_hot(100, 0)
print icy_hot(101, -1)
print icy_hot(101, 12)
print icy_hot(10, 123)
print icy_hot(-2, 103)

def closer_to(a, b, c):
	guess1 = a - b
	guess2 = a - c
	if abs(guess1) > abs(guess2):
		return c
	if abs(guess1) < abs(guess2):
		return b
	if abs(guess1) == abs(guess2):
		return 0
print closer_to(321, 123, 234)
print closer_to(321, 323, 12)
print closer_to(321, 321, 321)
print closer_to(321, 319, 323)

def two_as_one(a, b, c):
	if a + b == c:
		return True
	if b + c == a:
		return True
	if a + c == b:
		return True
	else:
		return False
print two_as_one(1, 2, 3) 
print two_as_one(1, 3, 2) 
print two_as_one(3, 1, 2) 
print two_as_one(3, 1, 56) 

def pig_latinify(str):
	if (str[0] == "a") or (str[0] == "e") or (str[0] == "i") or (str[0] == "o") or (str[0] == "u") or (str[0] == "y") or (str[0] == "A") or (str[0] == "E") or (str[0] == "I") or (str[0] == "O") or (str[0] == "U") or (str[0] == "Y"):
	 	bl = str + "way"
	 	return bl.lower()
	if (str[0] == "b") or (str[0] == "c") or (str[0] == "d") or  (str[0] == "f") or (str[0] == "g") or (str[0] == "h") or (str[0] == "j") or (str[0] == "k") or (str[0] == "l") or (str[0] == "m") or (str[0] == "n") or (str[0] == "p") or (str[0] == "q") or (str[0] == "r") or (str[0] == "s") or (str[0] == "t") or (str[0] == "v") or (str[0] == "w") or (str[0] == "x") or (str[0] == "z") or (str[0] == "B") or (str[0] == "C") or (str[0] == "D") or (str[0] == "F") or (str[0] == "G") or (str[0] == "H") or (str[0] == "J") or (str[0] == "K") or (str[0] == "L") or (str[0] == "M") or (str[0] == "N") or (str[0] == "P") or (str[0] == "Q") or (str[0] == "R") or (str[0] == "S") or (str[0] == "T") or (str[0] == "V") or (str[0] == "W") or (str[0] == "X") or (str[0] == "Z"):
	 	br = str[1:] + str[0] + "ay"
	 	return br.lower()
print pig_latinify("aPple")
print pig_latinify("BURGERKINGBABY")
print pig_latinify("SmeLL")