#Given an array of N integers, can you find the sum of its elements?
#
#Input Format
#
#The first line contains an integer, N, denoting the size of the array.
#The second line contains N space-separated integers representing the array's elements.
#
#Output Format
#
#Print the sum of the array's elements as a single integer.
#
#Sample Input
#
#6
#1 2 3 4 10 11
#
#Sample Output
#
#31
#
#Explanation
#We print the sum of the array's elements, which is: 1+2+3+4+10+11=31.

n = gets.strip.to_i
arr = gets.strip
arr = arr.split(' ').map(&:to_i)
sum = 0

arr.each do |i|
  sum += i
end

p sum


#You are given an array of integers of size N. You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

#Input

#The first line of the input consists of an integer N. The next line contains N space-separated integers contained in the array.

#Constraints
#1<=N<=10
#0<=A[i]<=10^10

#Sample Input
#5
#1000000001 1000000002 1000000003 1000000004 1000000005

#Output
#Print a single value equal to the sum of the elements in the array. In the above sample, you would print 5000000015.

#Note: The range of the 32-bit integer is (-2^31)to(2^31-1) or [-2147483648, 2147483647]. When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.

n = gets.strip.to_i
arr = gets.strip
arr = arr.split(' ').map(&:to_i)

sum = 0
i = 0
while i < n do
  sum += arr[i]
  i += 1
end

p sum
