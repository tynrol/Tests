def solution(input_str):
	count_open = 0
	count_close = 0 
	opened = ''
	for char in input_str:
		#count openining and closing brackets
		if char == '(' or char == '[' or char == '{':
			count_open += 1
			opened += char
		if char == ')' or char == ']' or char == '}':
			#checking for opening brakets for this closing 
			if opened == '': 
				return False
			count_close += 1
			#checking if the last breacket is the same type
			if opened[-1]+char != '()' and opened[-1]+char != '[]' and opened[-1]+char != '{}':
				return False
			opened = opened[0:-1]
	if count_open != count_close:
		return False
	return True


input = input()
result = solution(input)
print(result)