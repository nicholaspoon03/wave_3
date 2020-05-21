text = input()
latin = text

if text[0] in 'aeiou':
    vowel = True
else:
    vowel = False

if vowel:
    latin += 'way'
else:
    for n in range(len(text)):
        if text[n] in 'aeiou':
            break
    first = text[:n]
    last = text[n:]
    latin = last + first + 'ay'

print(latin)