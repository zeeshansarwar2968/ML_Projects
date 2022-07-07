# NumPy Exercises

> 1. Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
> Expected Output:
> Original List: [12.23, 13.32, 100, 36.32]
> One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
> 
> 2. Create a 3x3 matrix with values ranging from 2 to 10.
> Expected Output:
> [[ 2 3 4]
> [ 5 6 7]
> [ 8 9 10]]
> 
> 3. Write a Python program to create a null vector of size 10 and update sixth value to 11.
> [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
> Update sixth value to 11
> [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
> 
> 4. Write a Python program to reverse an array (first element becomes last).
> Original array:
> [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
> Reverse array:
> [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]

> 5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
> Expected Output:
> Original array:
> [[ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]]
> 1 on the border and 0 inside in the array
> [[ 1. 1. 1. 1. 1.]
> [ 1. 0. 0. 0. 1.]
> [ 1. 0. 0. 0. 1.]
> [ 1. 0. 0. 0. 1.]
> [ 1. 1. 1. 1. 1.]]
> 
> 6. Write a Python program to add a border (filled with 0's) around an existing array.
> Expected Output:
> Original array:
> [[ 1. 1. 1.]
> [ 1. 1. 1.]
> [ 1. 1. 1.]]
> 1 on the border and 0 inside in the array
> [[ 0. 0. 0. 0. 0.]
> [ 0. 1. 1. 1. 0.]
> [ 0. 1. 1. 1. 0.]
> [ 0. 1. 1. 1. 0.]
> [ 0. 0. 0. 0. 0.]]
> 
> 7. Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
> Checkerboard pattern:
> [[0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]
> [0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]
> [0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]
> [0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]]
> 
> 8. Write a Python program to convert a list and tuple into arrays.
> List to array:
> [1 2 3 4 5 6 7 8]
> Tuple to array:
> [[8 4 6]
> [1 2 3]]
> 
> 9. Write a Python program to append values to the end of an array.
> Expected Output:
> Original array:
> [10, 20, 30]
> After append values to the end of the array:
> [10 20 30 40 50 60 70 80 90]
> 
> 10. Write a Python program to find the real and imaginary parts of an array of complex
> numbers.
> Expected Output:
> Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
> Real part of the array:
> [ 1. 0.70710678]
> Imaginary part of the array:
> [ 0. 0.70710678]
> 
> 11. Write a Python program to find the number of elements of an array, length of one
> array element in bytes and total bytes consumed by the elements.
> Expected Output:
> Size of the array: 3
> Length of one array element in bytes: 8
> Total bytes consumed by the elements of the array: 24
> 
> 12. Write a Python program to find common values between two arrays.
> Expected Output:
> Array1: [ 0 10 20 40 60]
> Array2: [10, 30, 40]
> Common values between two arrays:
> [10 40]
> 
> 13. Write a Python program to find the set difference of two arrays. The set difference
> will return the sorted, unique values in array1 that are not in array2.
> Expected Output:
> Array1: [ 0 10 20 40 60 80]
> Array2: [10, 30, 40, 50, 70, 90]
> Set difference between two arrays: [ 0 20 60 80]
> 
> 14. Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or
> will return the sorted, unique values that are in only one (not both) of the input arrays.
> Array1: [ 0 10 20 40 60 80]
> Array2: [10, 30, 40, 50, 70]
> Unique values that are in only one (not both) of the input arrays:
> [ 0 20 30 50 60 70 80]
> 
> 15. Write a Python program compare two arrays using numpy.
> Array a: [1 2]
> Array b: [4 5]
> a > b
> [False False]
> a >= b
> [False False]
> a < b
> [ True True]
> a <= b
> [ True True]
> 
> 16. Write a Python program to create a contiguous flattened array.
> Original array:
> [[10 20 30]
> [20 40 50]]
> New flattened array:
> [10 20 30 20 40 50]
> 
> 17. Write a Python program to change the data type of an array.
> Expected Output:
> [[ 2 4 6]
> [ 6 8 10]]
> Data type of the array x is: int32
> New Type: float64
> [[ 2. 4. 6.]
> [ 6. 8. 10.]]
> 
> 18. Write a Python program to create a 3-D array with ones on a diagonal and zeros
> elsewhere.
> Expected Output:
> [[ 1. 0. 0.]
> [ 0. 1. 0.]
> [ 0. 0. 1.]]
> 
> 19. Write a Python program to create an array which looks like below array.
> Expected Output:
> [[ 0. 0. 0.]
> [ 1. 0. 0.]
> [ 1. 1. 0.]
> [ 1. 1. 1.]]
> 
> 20. Write a Python program to concatenate two 2-dimensional arrays.
> Expected Output:
> Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
> Expected Output:
> [[ 0 1 3 0 2 4]
> [ 5 7 9 6 8 10]]
> 
> 21. Write a Python program to make an array immutable (read-only).
> Expected Output:
> Test the array is read-only or not:
> Try to change the value of the first element:
> Traceback (most recent call last):
> File "19236bd0-0bd9-11e7-a232-c706d0968eb6.py", line 6, in
> x[0] = 1
> ValueError: assignment destination is read-only
> 
> 22. Write a Python program to create an array of (3, 4) shape, multiply every element
> value by 3 and display the new array.
> Expected Output:
> Original array elements:
> [[ 0 1 2 3]
> [ 4 5 6 7]
> [ 8 9 10 11]]
> New array elements:
> [[ 0 3 6 9]
> [12 15 18 21]
> [24 27 30 33]]
> 
> 23. Write a Python program to convert a NumPy array into Python list structure.
> Expected Output:
> Original array elements:
> [[0 1]
> [2 3]
> [4 5]]
> Array to list:
> [[0, 1], [2, 3], [4, 5]]
> 
> 24. Write a Python program to convert a NumPy array into Python list structure.
> Expected Output:
> Original array elements:
> [ 0.26153123 0.52760141 0.5718299 0.5927067 0.7831874 0.69746349
> 0.35399976 0.99469633 0.0694458 0.54711478]
> Print array values with precision 3:
> [ 0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]
> 
> 25. Write a Python program to suppresses the use of scientific notation for small
> numbers in numpy array.
> Expected Output:
> Original array elements:
> [ 1.60000000e-10 1.60000000e+00 1.20000000e+03 2.35000000e-01]
> Print array values with precision 3:
> [ 0. 1.6 1200. 0.235]
> 
> 26. Write a Python program to how to add an extra column to an numpy array.
> Expected Output:
> [[ 10 20 30 100]
> [ 40 50 60 200]]
> 
> 27. Write a Python program to remove specific elements in a numpy array.
> Expected Output:
> Original array:
> [ 10 20 30 40 50 60 70 80 90 100]
> Delete first, fourth and fifth elements:
> [ 20 30 60 70 80 90 100]
> 
> 28. Write a Python program to save a NumPy array to a text file.