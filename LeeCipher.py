#lees cipher. Use it to send & recieve encrypted messages with your friends!
#TO-DO further encrypt the text with a random pass generator that links to more def functions...

cypher1 = [["b"],["a"],["c"],["d"],["i"],["f"],["j"],["h"],["e"],["g"],["k"],["n"],["m"],["l"],["u"],["p"],["x"],["r"],["z"],["t"],["o"],["v"],["w"],["q"],["y"],["s"]]
cypher2 = [["2"],["6"],["b"],["7"],["v"],["w"],["j"],["n"],["z"],["l"],["q"],["e"],["0"],["g"],["i"],["u"],["t"],["f"],["x"],["o"],["3"],["4"],["9"],["p"],["h"],["y"]]
#a = 6 = 1 #b = 2 = 0 #c = b = 2 #d = 7 = 3 #e = z = 8
#f = w = 5 #g = 1 = 9 #h = n = 7 #i = v = 4 #j = j = 6
#k = q = 10 #l = g = 13 #m = 0 = 12 #n = e = 11 #o = 3 = 20
#p = u = 15 #q = p = 23 #r = f = 17 #s = y = 25 #t = o = 19
#u = i = 14 #v = 4 = 21 #w = 9 = 22 #x = t = 16
#y = h = 24 #z = x = 18

def cyph(let):
	if let == "b":
                return print(cypher2[0],end="")
        if let == "a":
                return print(cypher2[1],end="")
        if let == "c":
                return print(cypher2[2],end="")
        if let == "d":
                return print(cypher2[3],end="")
        if let == "e":
                return print(cypher2[8],end="")
        if let == "f":
                return print(cypher2[5],end="")
        if let == "g":
                return print(cypher2[9],end="")
        if let == "h":
                return print(cypher2[7],end="")
        if let == "i":
                return print(cypher2[4],end="")
        if let == "j":
                return print(cypher2[6],end="")
        if let == "k":
                return print(cypher2[10],end="")
        if let == "l":
                return print(cypher2[13],end="")
        if let == "m":
                return print(cypher2[12],end="")
        if let == "n":
                return print(cypher2[11],end="")
        if let == "o":
                return print(cypher2[20],end="")
        if let == "p":
                return print(cypher2[15],end="")
        if let == "q":
                return print(cypher2[23],end="")
        if let == "r":
                return print(cypher2[17],end="")
        if let == "s":
                return print(cypher2[25],end="")
        if let == "t":
                return print(cypher2[19],end="")
        if let == "u":
                return print(cypher2[14],end="")
        if let == "v":
                return print(cypher2[21],end="")
        if let == "w":
                return print(cypher2[22],end="")
        if let == "x":
                return print(cypher2[16],end="")
        if let == "y":
                return print(cypher2[24],end="")
        if let == "z":
                return print(cypher2[25],end="")

def cyph2(read):
	if read == "['2']" or read == "2":
		return print(cypher1[0],end="")
	if read == "6" or read == "['6']":
		return print(cypher1[1],end="")
	if read == "b" or read == "['b']":
		return print(cypher1[2],end="")
	if read == "7" or read == "['7']":
		return print(cypher1[3],end="")
	if read == "z" or read == "['z']":
		return print(cypher1[8],end="")
	if read == "w" or read == "['w']":
		return print(cypher1[5],end="")
	if read == "l" or read == "['l']":
		return print(cypher1[9],end="")
	if read == "n" or read == "['n']":
		return print(cypher1[7],end="")
	if read == "z" or read == "['z']":
		return print(cypher1[8],end="")
	if read == "w" or read == "['w']":
		return print(cypher1[5],end="")
	if read == "l" or read == "['l']":
		return print(cypher1[9],end="")
	if read == "n" or read == "['n']":
		return print(cypher1[7],end="")
	if read == "v" or read == "['v']":
		return print(cypher1[4],end="")
	if read == "j" or read == "['j']":
		return print(cypher1[6],end="")
	if read == "q" or read == "['q']":
		return print(cypher1[10],end="")
	if read == "g" or read == "['g']":
		return print(cypher1[13],end="")
	if read == "0" or read == "['0']":
		return print(cypher1[12],end="")
	if read == "e" or read == "['e']":
		return print(cypher1[11],end="")
	if read == "3" or read == "['3']":
		return print(cypher1[20],end="")
	if read == "u" or read == "['u']":
		return print(cypher1[15],end="")
	if read == "p" or read == "['p']":
		return print(cypher1[23],end="")
	if read == "f" or read == "['f']":
		return print(cypher1[17],end="")
	if read == "y" or read == "['y']":
		return print(cypher1[25],end="")
	if read == "o" or read == "['o']":
		return print(cypher1[19],end="")
	if read == "i" or read == "['i']":
		return print(cypher1[14],end="")
	if read == "4" or read == "['4']":
		return print(cypher1[21],end="")
	if read == "9" or read == "['9']":
		return print(cypher1[22],end="")
	if read == "t" or read == "['t']":
		return print(cypher1[16],end="")
	if read == "h" or read == "['h']":
		return print(cypher1[24],end="")
	if read == "x" or read == "['x']":
		return print(cypher1[25],end="")
def Main():
	ask1 = input("Write or Read (W or R) Coded Cyper Message?: ")
	if ask1.upper() == "W":
		message = input("Your message: ")
		for i in message.strip().lower():
			cyph(i)
	elif ask1.upper() == "R":
		read = input("Read: ")
		for i in read.strip().lower():
			cyph2(i)
if __name__ == "__main__":
	Main()
