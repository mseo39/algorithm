# def get_peek(a,low,high,n):

#     if low<=high:
#         mid=(low+high)//2
#         print("현재 배열")
#         print(a[low:high + 1])
#         print(a[mid])

#         if((a[mid]>=a[mid-1] and a[mid]>=a[mid+1]) or (mid==n and a[mid-1]<=a[mid]) or (mid==0 and a[mid]>=a[mid+1])):
#             print("====>", end="")
#             print(a[mid])
#         print("\n\n")

#         if low==mid and high==mid:
#             return 0
            
#         get_peek(a,low,mid,n)
#         get_peek(a,mid+1,high,n)
#     else:
#         return 0

# get_peek([8,9,10,2,5,6],0,5,5)

def get_peak(a, start, end):
    mid = (start + end) // 2

    if (mid == 0 or a[mid] >= a[mid - 1]) and (mid == len(a) - 1 or a[mid] >= a[mid + 1]):
        # 현재 원소가 피크인 경우
        print(a[mid])
    elif mid > 0 and a[mid - 1] > a[mid]:
        # mid를 기준으로 왼쪽 부분 배열에서 피크 원소를 찾는다
        return get_peak(a, start, mid - 1)
    else:
        # mid를 기준으로 오른쪽 부분 배열에서 피크 원소를 찾는다
        return get_peak(a, mid + 1, end)


def find_peak(a):
    n = len(a)
    return get_peak(a, 0, n - 1)

find_peak([8,9,10,2,5,6])
