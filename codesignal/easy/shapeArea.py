# https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

# def shapeArea(n):
#     # start = 1
#     area = 0
#     if n <= 1:
#         return n
#     else:
#         area = 1
#         for i in range(2, n+1):
#             print(i)
#             area = area + 2**i
#             print(area)
#     return area

def shapeArea(n):
    if n>=10**4 or n<1:
        return False

    return (n**2+(n-1)**2)