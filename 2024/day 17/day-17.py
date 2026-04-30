

with open("puzzle17.txt", 'r') as file:
    data = file.readlines()

A = int(data[0].split(':')[1])
B = int(data[1].split(':')[1])
C = int(data[2].split(':')[1])
# print(A, B, C)

comands = list(map(int, data[-1].split(':')[-1].split(',')))
print(f"comands: {comands}")


def func(A, B, C):

    combos = [0, 1, 2, 3, A, B, C]
    ans = []
    i = 0

    while i < len(comands):
        if comands[i] == 0:
            A = A // (2 ** combos[comands[i+1]])
            combos[4] = A

        elif comands[i] == 1:
            B = B ^ comands[i+1]
            combos[5] = B


        elif comands[i] == 2:
            B = combos[comands[i+1]] % 8
            combos[5] = B

        elif comands[i] == 3:
            if A != 0:
                i = comands[i+1]
                continue

        elif comands[i] == 4:
            B = B ^ C
            combos[5] = B

        elif comands[i] == 5:
            ans.append(combos[comands[i+1]] % 8)

        elif comands[i] == 6:
            B = A // (2 ** combos[comands[i+1]])
            combos[5] = B

        elif comands[i] == 7:
            C = A // (2 ** combos[comands[i+1]])
            combos[6] = 6
            
        i += 2

    return ans



# A = 164541160582845
# ans = func(A, B, C)
# print(ans)



def rec(A, comands, k, ans):


    if k < 0 - len(comands):
        return False

    print(A)

    for i in range(8):
        ans = func(A + i, B, C)
        if ans == comands[k:]:
            if ans == comands:
                print(f"qwertyuii: {A+i}")
                print(f"!!! {ans} !!!")
                return True

            t = rec(8*(A+i), comands, k-1, ans)

        
ans = rec(0, comands, -1, [])
# print(",".join(list(map(str, ans))))

