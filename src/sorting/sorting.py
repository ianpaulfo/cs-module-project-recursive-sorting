# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    indexa = 0
    indexb = 0
    for i in range(0, elements):
        if indexa >= len(arrA):
            merged_arr[i] = arrB[indexb]
            indexb += 1
        elif indexb >= len(arrB):
            merged_arr[i] = arrA[indexa]
            indexa += 1
        elif arrA[indexa] < arrB[indexb]:
            merged_arr[i] = arrA[indexa]
            indexa += 1
        else:
            merged_arr[i] = arrB[indexb]
            indexb += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    else:
        left=arr[: len(arr) // 2 ]
        right=arr[len(arr) // 2 :]
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

