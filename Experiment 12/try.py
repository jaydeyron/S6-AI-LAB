from itertools import permutations

exp1=input("Enter expression 1: ").upper()
exp2=input("Enter expression 2: ").upper()
result=input("Enter result: ").upper()
letters=set(exp1+exp2+result)

for permutation in permutations("0123456789",len(letters)):
    perm=dict(zip(letters,permutation))
    new_exp1=exp1
    new_exp2=exp2
    new_result=result
    for key,value in perm.items():
        new_exp1=new_exp1.replace(key,value)
        new_exp2=new_exp2.replace(key,value)
        new_result=new_result.replace(key,value)
    if new_exp1.startswith("0") or new_exp2.startswith("0") or new_result.startswith("0"):
        continue
    if int(new_exp1)+int(new_exp2)==int(new_result):
        print(f"{exp1}={new_exp1}\n{exp2}={new_exp2}\n{result}={new_result}")
        print(perm,"\n")
        exit()