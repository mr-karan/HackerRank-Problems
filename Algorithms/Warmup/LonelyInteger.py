n=input()
arr = sorted(map(int, raw_input().strip().split(" ")))


if len(arr)==1:
    ans=arr[0]
for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        continue
    else:
        ans = arr[i + 1]

print ans
