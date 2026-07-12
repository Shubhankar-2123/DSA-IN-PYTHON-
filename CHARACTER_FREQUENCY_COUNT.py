s = "azyxyyzaaaa"

q = ['d','a','y' ,'x']

freq_count= {}
for x in s:
    if x not in freq_count:
        freq_count[x] = 1
    else:
        freq_count[x] += 1

for x in q :
    if x not in freq_count:
        print(f"Occurence of {x} is 0")
    else :
        print(f"occurence of {x} is {freq_count[x]}")
print(freq_count)