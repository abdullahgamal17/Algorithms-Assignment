#20198007 Ahmed Mohamed
#20198054 Abdullah Gamal
#20198083 Mostafa Mohamed

import numpy as np
import math
import copy
#####################################################
# 1) write the function to do insertion sort
def insertion_sort(arr):
    size = len(arr)
    swapping = 0
    for i in range(1, size):
        k = arr[i]
        j = i-1
        
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            swapping += 1
            j -= 1
        arr[j+1] = k
           
    return arr , swapping
    
#####################################################
# 2) Problem 2
def get_random(m_w,m_z):
    x = (m_z & 65535)
    y = (m_z >> 16)
    a = (m_w & 65535)
    b = (m_w >> 16)
    m_z = 36969 * x + y 
    m_w = 18000 * a + b 
    res = ((m_z << 16) + m_w)
    res = res % 1000000000
    return res , m_w , m_z

#write quick sort
def partition(arr,left,right):
    pivot_index = left
    pivot = arr[pivot_index]
    
    while left < right:
        while left < len(arr) and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
        arr[right],arr[pivot_index] = arr[pivot_index],arr[right]
        
        return right

def quick_sort(arr,left,right):
    
    if left < right:
        pivot_index = partition(arr,left,right)
        quick_sort(arr,left,pivot_index-1)
        quick_sort(arr,pivot_index+1,right)
    
    return arr

def problem_2(N,k,m_w,m_z):
    arr = []
    for i in range(N):
        ans = get_random(m_w,m_z)
        arr.append(ans[0])
        m_w = ans[1]
        m_z = ans[2] 
    
    left = 0
    right = len(arr)-1
    arr = quick_sort(arr,left,right)
    answer = arr[k-1]
    return answer

answer = problem_2(3,2,1,2)
print(answer)
#####################################################
#3) Problem 3

def merge(arr,temp,left,mid,right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    
    
    while((i <= mid) and (j <= right)):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            inv_count+=(mid- i+ 1)
            k+=1
            j+=1
    
    while i <= mid:
        temp[k] = arr[i]
        k+=1
        i+=1
    while j <= right:
        temp[k] = arr[j]
        k+=1
        j+=1
    for i in range(left,right+1):
        arr[i] = temp[i]
    
    return inv_count
                  
def _mergesort(arr,temp,left,right):
    inv_count = 0
    if right > left:
        mid = (right+left)//2
        inv_count += _mergesort(arr,temp,left,mid)
        inv_count += _mergesort(arr,temp,mid+1,right)
        inv_count += merge(arr,temp,left,mid,right)
        
    return inv_count
        
def mergesort(arr):
    size = len(arr)
    temp = [0]*size
    x = _mergesort(arr,temp,0,size-1)
    return x

arr = [1,2,3,4]
arr2 = [2,1]
arr3 = [3,2,1,4]

print(mergesort(arr))
print(mergesort(arr2))
print(mergesort(arr3))
  
#####################################################
#4) Problem 4
input_arr = [1,4,1,1]
def operation1(arr,l,r):
    for i in range(l,r+1):
        if(arr[i] > 0):
            arr[i] -= 1
    return arr

def operation2(arr,i,x):
    arr[i] -= x
    return arr
def problem4(inp):
    count = 0
    while True:
        _max = max(inp)
        _max_index = inp.index(_max)
        _min = min(inp)
        _min_index = inp.index(_min)
        l = 0
        r = len(inp)-1
        x = _max - 1
        if _max == 0 and _min == 0:
            return count
        for i in range(len(inp)):
            if inp[i] > 0:
                l = i
                break
        for i in range(l,len(inp)):
            if inp[i] == 0 and i >= l:
                r = i
                break
            
        if _max != 1:
            inp = operation2(inp,_max_index,x)
            count += 1
        else:
            inp = operation1(inp,l,r)
            count += 1
        

print(problem4(input_arr))
#####################################################             
#5) Problem 5
import skiplist as sp
mylist = sp.skip_list()
mylist.insert_node(2)
mylist.insert_node(10)
mylist.insert_node(15)
mylist.insert_node(16)
mylist.insert_node(31)
mylist.insert_node(71)
mylist.insert_node(89)
mylist.insert_node(91)
mylist.insert_node(96)
mylist.print_list()
print(mylist.get_layers())
mylist.print_level(2)

#####################################################
#6) Problem 6
table1 = [("XDFSE1","Jack","Electronics"),("XDVBA2","Mary","Aesthetics")]
table2 = [("TV","XDFSE1","Mark"),("Radio","XDFSE1","Susan"),("Skincare Ointment","XDVBA2","Lisa")]
def problem6(table1,table2):
    m = len(table2)
    arr = [0]*m
    ids ={}
    for i in range(len(table1)):
        ids[table1[i][0]]  = i
    
    for i in range(m):
        arr[i] = ids[table2[i][1]]
    return arr

print(problem6(table1,table2))
#####################################################
def problem7(X,Y,X_dash,Y_dash,a,b):
    ret_x = a*(X+X_dash) 
    ret_y = b*(Y+Y_dash)
    
#####################################################
#7) Problem 8
#The fastest way is using binary search to find a defective toy , because its complexity is lgn
#then going back one step at a time till meeting a non defective toy 
#the first defective toy is the one after the first non defective toy we meet
#####################################################
#9) Problem 9
list = []
def operation1_p9(list,value):
    list.append(value)
    list = sorted(list)
    return list

def operation2_p9(list,l,r,x):
    while l <= r:
        mid = (l+r)//2
        if list[mid] == x:
            return mid
        elif list[mid] < x:
            l = mid+1
        else:
            r = mid-1
    
    return -1
    
def problem9(Q):
    mylist = []
    answer = []
    for i in range(Q):
        inp = input()
        command = int(inp.split()[0])
        value = int(inp.split()[1])
        if command == 1:
            mylist = operation1_p9(mylist,value)
        elif command == 2:
            index = operation2_p9(mylist,0,len(mylist)-1,value)
            if index != -1:
                answer.append(index+1)
            else:
                answer.append(index)
        else:
            print("Invalid")
    print(answer)
            
problem9(10)            

#####################################################

#####################################################
#11)problem 11
def coin_row(coins, n):
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    return max(coin_row(coins, n-1), coin_row(coins, n-2) + coins[n-1])

coins = [3,5,-7,8,10]
print(coin_row(coins, len(coins)))
#################################################
def Euclidean_distance(p,q):
    distance = np.sqrt( pow((q[0]-p[0]),2) + pow((q[1]-p[1]),2) )
    return distance
#Find the minimum distance between two points in O(nlgn)    
def smallest_distance(plane):
    pass
#################################################
def Backtrack(i, j):
    if (i == j):
        print("A", i, end='')
    else:
        print("(", end='')
        Backtrack(i, int(backtrack[i][j]))
        print(" x ", end='')
        Backtrack(int(backtrack[i][j]+1), j)
        print(")", end='')


num = 0


def matrix(arr):
    n = (len(arr)//2)+1
    number_of_matrices = len(arr)//2
    empty_string = ""
    for i in range(number_of_matrices):
        empty_string += "A"+str(i+1)+" "

    p = [0]*n
    p[0] = arr[0]
    x = 1
    for i in range(1, n):
        p[i] = arr[x]
        x += 2
    m = np.zeros((n, n))
    backtrack = np.zeros((n, n))
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i+d
            _min = 500000
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < _min:
                    _min = q
                    backtrack[i][j] = k
            m[i][j] = _min
    return backtrack


arr = []
arr = [int(item) for item in input().split()]
backtrack = matrix(arr)


num = len(arr)//2
Backtrack(1, num)
#################################################
#problem 12
class MY_Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
def Euclidean_distance (point1, point2):
    return math.sqrt(pow((point1.x - point2.x),2) + pow((point1.y - point2.y),2))
                     
# The brute force techniqe if their is 3 or two points only in  the plane
def Brute_Force(Point, num_of_points):
    minimum_distance = 10000000.0
    for i in range(num_of_points):
        for j in range(i + 1, num_of_points):
            if Euclidean_distance (Point[i], Point[j]) < minimum_distance:
                minimum_distance = Euclidean_distance (Point[i], Point[j])
    return minimum_distance
 
# Find the smallest distance in the strip and return it if it smaller than d
def Smallest_d_in_strip(strip, num_of_points, d):
    minimum_distance = d
    
    for i in range(num_of_points):
        j = i + 1
        while j < num_of_points and (strip[j].y - strip[i].y) < minimum_distance:
            minimum_distance = Euclidean_distance(strip[i], strip[j])
            j += 1
 
    return minimum_distance
 
# Find the smallest distance in my plane between two points.
# plane_x : is ordered plane according to x axis 
# plane_y : is an orded plane according to y axis 
def Smallest_distance(plane_x,  plane_y,  num_of_points):

    # Use brute force if their is two or three points only in the plane 
    if num_of_points <= 3:
        return Brute_Force(plane_x, num_of_points)
 
    # Find the middle point
    middle_position = num_of_points // 2
    middle_Point = plane_x[middle_position]
 
    # Divide my plane into two planes (Right and left)
    left_plane = plane_x[:middle_position]
    right_plane = plane_x[middle_position:]
 
    # d_l : is the smallest distance in left plane 
    # d_r : is the smallest distance in right plane
    # using the recurcion 
    d_l = Smallest_distance(left_plane, plane_y, middle_position)
    d_r = Smallest_distance(right_plane, plane_y, num_of_points - middle_position)
 
    d = min(d_l, d_r)
 
    # Build an array strip[] that contains the points that its distance between it and the middle line is smaller than d
    # strip_x : the strip which ordered according to x axis 
    strip_x = []
    
    left_and_right = left_plane + right_plane
    for i in range(num_of_points):
        if abs(left_and_right[i].x - middle_Point.x) < d:
            strip_x.append(left_and_right[i])

    # Sorting strip_x according to y axis
    strip_x.sort(key = lambda MY_Point: MY_Point.y) 
    
    #get the minimum distance between (d from stip_x) and the d from right or left plane 
    minimum_distance_1 = min(d, Smallest_d_in_strip(strip_x, len(strip_x), d))

    
    # Return the final answer
    return (minimum_distance_1)
    # return min(minimum_distance_1,minimum_distance_2)

def Main(array_of_points , num_of_points):
    array_of_points.sort(key = lambda MY_Point: MY_Point.x)
    
    # array_y : is a deep copy of array_of_points to sort the points in this array according to y axis 
    array_y = copy.deepcopy(array_of_points)
    array_y.sort(key = lambda MY_Point: MY_Point.y)   
 
    # Find the smallest distance by using Smallest_distance function
    return Smallest_distance(array_of_points, array_y, num_of_points)
 
arr = [MY_Point(20, 30), MY_Point(5, 30), MY_Point(46, 54), MY_Point(53, 21), MY_Point(42, 12), MY_Point(13, 34)]
n = len(arr)
print("The smallest distance is",Main(arr, n))
#################################################
#14) Problem 14
def printPairs(arr, size, target):
    count = 0
    # Create an empty hash set
    Hash_table = set()
     
    for i in range(0, size):
        temp = target-arr[i]
        if (count == 0):
            if (temp in Hash_table):
                print ("Pair found ("+ str(arr[i]) + ", " + str(temp) + ")", end='')
                count +=1
                i+=1
        else:
            if (temp in Hash_table):
                print (" OR Pair found ("+ str(arr[i]) + ", " + str(temp) + ")")
        Hash_table.add(arr[i])
    if (count == 0):
        print ("Pair not found")

arr = []
arr = [int(item) for item in input().split()]

target = int (input())
printPairs(arr, len(arr), target)
#################################################
#15) problem 15
def problem_15(arr):
 
    minimum_index = len(arr)
    
    my_Repository = set()
    for i in reversed(range(len(arr))):
        if arr[i] in my_Repository:
            minimum_index = i
        else:
            my_Repository.add(arr[i])

    return minimum_index
 

arr = []
arr = [int(item) for item in input().split()]

minimum_index = problem_15(arr)
 
if minimum_index != len(arr):
    print("The minimum index of the repeating element is", minimum_index)
else:
    print("Invalid Input")

#################################################