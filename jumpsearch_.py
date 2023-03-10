# SEARCHING JUMPSEARCH

def jumpSearch(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    for c in range(len(arr)):
            if type(arr[c])==list:
                a = jumpSearch(arr[c],x)
                if a == -1:
                    print('Menemukan Data')
                else:
                    print(f'{x} ada pada indeks {c} kolom {a}')
                    exit()
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1 
    if arr[prev] == x:
        return prev
    return -1

arr = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
print(arr)
x = input('Masukan nama yang dicari: ')
b = jumpSearch(arr,x)
if b == -1:
    print('Nama tidak ditemukan')
else:
    print(f'{x} Nama ada pada indeks {b}')

