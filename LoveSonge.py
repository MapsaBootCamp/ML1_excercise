from typing import Sequence


def separate(sentence:str,n:int, m:int):
    new_sentence=sentence[n-1:m]
    return new_sentence

def index(sentence:str):
    en_alpahbet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index=en_alpahbet.index(sentence)
    return index

def result(sentence:str,n:int, m:int):
    new_sep=separate(sentence,n,m)
    count_list=[]
    for i in new_sep:
        count_list.append(index(i)+1)
        sum_index=sum(count_list)
    return sum_index



n,q=map(int,input().split())
client_Sequence=input()
for i in range(q):
    l,r=map(int,input().split())
    print(result(client_Sequence,l,r))

