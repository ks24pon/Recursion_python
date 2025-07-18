def getMaxIndex(arr):
    # 関数を完成させてください
    maxValueIndex = 0
    for i in range(len(arr)):
        if arr[i] >= arr[maxValueIndex]:
            maxValueIndex = i
    return maxValueIndex