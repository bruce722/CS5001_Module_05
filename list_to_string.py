from functools import reduce

def list_to_string(input_list):
	if isinstance(input_list, list) and len(input_list) > 0:
		return reduce(lambda a, b: str(a)+"\n"+str(b), input_list)
	else:
		return ""

if __name__ == '__main__':
	print(list_to_string([]))
	print(list_to_string(["khoury", "college", "align", "masters"]))