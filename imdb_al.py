import csv

def insertion_sort(lst):
    for i in range(1, len(lst)):
        ini = lst[i]
        j = i - 1
        while j >= 0 and float(ini[1]) < float(lst[j][1]):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = ini
    return lst

def hybrid_sorting(arr):
    if len(arr) < 32:
        return arr
    mid = len(arr) // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:]
    sorted_arr1 = hybrid_sorting(arr1)
    sorted_arr2 = hybrid_sorting(arr2)
    return insertion_sort(sorted_arr1 + sorted_arr2)

def binary_search(lst, rating):
    low = 0
    high = len(lst) - 1
    rating = float(rating)
    while True:
        mid = low + ((high - low) // 2)
        if (mid_val := float(lst[mid][1])) == rating:
            high = mid
        elif mid_val > rating:
            high = mid - 1
        elif mid_val < rating:
            low = mid + 1
        if low == mid:
            return mid
        
movies_lst = []
with open('movies.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        movies_lst.append((row[0], row[1]))
    movies_lst = hybrid_sorting(movies_lst)
    print(movies_lst)
    for movie in movies_lst[binary_search(movies_lst, '6.0'):]:
        if float(movie[1]) != 6.0:
            break
        else:
            name, rating = movie
            print(f'{name} - {rating}')
