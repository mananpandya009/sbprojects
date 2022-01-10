def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    arr_len = len(nums)
    for i in range(arr_len):
        if nums[i] == 7:
            print("should be true")
            break
        elif i == (arr_len-1):
            print("should be false")
            


any7([1,2,3])
any7([1,2,3,7])

