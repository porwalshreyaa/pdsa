'''
Q1
Given an array arr[] of n positive integers which can contain integers from 1 to p where elements can be repeated or can be absent from the array.
Your task is to count the frequency of all numbers from 1 to n. Do modify the array in-place changes in arr[], such that are[i]=frequency(i) and assume 1-based indexing.

note:
the elements greater than n can be ignored for counting 

example
input: n=5 arr[]={2,3,2,3,5} p=5
output: 0 2 2 0 1
1 occur 0 times
2 occur 2 times
3 occur 2 times
4 occur 0 times
5 occur 1 time

input: n=4 arr[]={3,3,3,3} p=3
output: 0 0 4 0
1 occur 0 times
2 occur 0 times
3 occur 4 times
4 occur 0 times

input: n=2 arr[]={8,9} p=9
output: 0 0
1 occur 0 times
2 occur 0 times 
since p is 9 but there are no 9th index present so can't count the value
'''


class Solution:
    def frequencyaCount(self, arr, N, P):
        d= [0]*N
        for i in arr:
            if 1 <= i <= N:
                arr[i]=d[i]
        return arr


'''
Q2
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

example


'''