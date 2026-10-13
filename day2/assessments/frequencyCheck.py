numbers=[1,1,1,2,3,4,21,44,13,44,10,12,43]
freq={}
for i in numbers:
    freq[i]=freq.get(i,0)+1
for number in freq:
    print(number,freq[number],sep=" -> ")