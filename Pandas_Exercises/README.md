# Pandas Exercises

> 1. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
> 
> 2. Write a Python program to convert a Panda module Series to Python list and it's type.
>    
> 3. Write a Python program to add, subtract, multiple and divide two Pandas Series.\
> Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
> 
> 4. Write a Python program to get the powers of an array values element-wise.\
> Note: First array elements raised to powers from second array\
> Expected Output:\
> Original array\
> [0 1 2 3 4 5 6]\
> First array elements raised to powers from second array, element-wise:\
> [ 0 1 8 27 64 125 216]
> 
> 5. Write a Python program to create and display a DataFrame from a specified dictionary\
> data which has the index labels.\
> Sample Python dictionary data and list labels:\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',\
> 'Matthew', 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 6. Write a Python program to display a summary of the basic information about a specified Data Frame and its data.
> Sample Python dictionary data and list labels:\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 7. Write a Python program to get the first 3 rows of a given DataFrame.\
> Sample Python dictionary data and list labels:\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes','no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 8. Write a Python program to select the 'name' and 'score' columns from the following DataFrame.\
> Sample Python dictionary data and list labels:\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 9. Write a Python program to select the specified columns and rows from a given data frame.\
> Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 10. Write a Python program to select the rows where the number of attempts in the examination is greater than 2.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 11. Write a Python program to count the number of rows and columns of a DataFrame.\
> Sample data:\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 12. Write a Python program to select the rows where the score is missing, i.e. is NaN.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 13. Write a Python program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
> 
> 14. Write a Python program to change the score in row 'd' to 11.5.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 15. Write a Python program to calculate the sum of the examination attempts by the students.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 16. Write a Python program to calculate the mean score for each different student in DataFrame.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 17. Write a Python program to append a new row 'k' to data frame with given values for\
> each column. Now delete the new row and return the original DataFrame.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\
> Values for each column will be:\
> name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
> 
> 18. Write a Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\
> Values for each column will be:\
> name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
> 
> 19. Write a Python program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 20. Write a Python program to delete the 'attempts' column from the DataFrame.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 21. Write a Python program to insert a new column in existing DataFrame.\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> 
> 22. Write a Python program to iterate over rows in a DataFrame.
> 
> 23. Write a Python program to get list from DataFrame column headers.\
> Sample data:\
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',\
> 'Laura', 'Kevin', 'Jonas'],\
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}\
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']