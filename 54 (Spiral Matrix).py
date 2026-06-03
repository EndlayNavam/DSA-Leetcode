class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        array=[]
        n = len(matrix) #len of matrix gives number of rows
        m = len(matrix[0]) #length of columns
        top, bottom = 0 , n-1 
        left, right = 0, m-1 

        while  len(array) < n*m: 
            #left --> right
            for i in range (left,right+1):
                array.append(matrix[top][i]) #row will be fixed, column will change
            top += 1

            if len(array) == n*m:
               break

            #top --> bottom
            for i in range (top,bottom+1):
                array.append(matrix[i][right]) #eow will change, column will be fix
            right -= 1

            if len(array) == n*m:
               break

            #right --> left
            for i in range (right,left-1,-1): #left is -1, to make sure last element of left is included
                array.append(matrix[bottom][i])
            bottom -= 1
            if len(array) == n*m:
               break

            #bottom --> top
            for i in range (bottom,top-1,-1): #top is -1, to make sure last element of to is included
                array.append(matrix[i][left])
            left += 1
            if len(array) == n*m:
               break
        return(array)