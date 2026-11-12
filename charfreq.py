data = "programming"

freq = {}
for ch in data:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1


# print(freq)
for key in freq:
    print(key," : ",freq[key])
# print('z' in freq)