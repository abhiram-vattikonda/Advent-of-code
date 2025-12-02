import time

start_time = time.time()

with open("inp2.txt") as f:
    ranges = f.read().split(",")

count = 0

# PART 1
# for rng in ranges:
#     print(f"Starting {rng}: ")
#     start, end = rng.split("-")
#     print(start, end)
#     for i in range(int(start), int(end) + 1):
#         i = str(i)
#         if i[:len(i)//2] == i[len(i)//2:]:
#             count += int(i)
#             print(i)
    
#     print("\n")



# PART 2
for rng in ranges: 
    print(f"Starting {rng}: ")
    start, end = rng.split("-")
    print(start, end)
    for i in range(int(start), int(end) + 1):
        i = str(i)
        for l in range(1, len(i)//2 + 1): # lenght of substring
            sub = i[0:l]
            pattern_present = True

            if (len(i)//l) * l != len(i):
                continue

            for p in range(0, (len(i)//l) - 1): # iterate through substrings
                if i[p * l : (p+1) * l] != i[(p+1) * l: (p+2) * l]:
                    pattern_present = False
                    break
            
            if pattern_present:
                count += int(i)
                print(i)
                break
    
    print("\n")
        


print(count)

print(f"----- {time.time() - start_time} -----")
    