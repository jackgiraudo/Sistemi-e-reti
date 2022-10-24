diz = {"a": "b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h", "h":"i", "i":"l ", "l":"m", "m":"n", "n":"o","o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", "v":"w", "w":"z" }
#decifra = {"z": "w", "w": "v", "v": "u", "u": "t", "t": "s", "s": "r", "r": "q", "q": "p", "p": "o", "o": "n", "n": "m", "m": "l", "l": "i", "i": "h", "h": "g", "g": "f", "f": "e", "e": "d", "d": "c", "c": "b", "b": "a", "a": "z", " ": " "}
stringa=input("inserire un nome")
scifrata=""
sdecifrata=""
sdecifrata=dict({})

#cifro la parola
for c in stringa:
    scifrata= scifrata + diz[c]

print(scifrata)

#decifro la parola
for k,v in diz.items():
    sdecifrata[v]=k

print(sdecifrata)
