N=int(input())

#입력받기
#단어 중복 맏기 위해 set으로
wordset=set()
for i in range(N):
    word=input()
    length=len(word)
    wordset.add((length,word))

#정렬하기
lst=list(wordset)
lst.sort()

#출력하기
for i in range(len(lst)):
    print(lst[i][1])