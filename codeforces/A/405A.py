columns = int(input())
size_columns = list(map(int, input().split()))
size_columns.sort()
 
result = ""
 
for value in size_columns:
	result += str(value) + " "
 
print(result.strip())