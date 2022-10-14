from functools import reduce

def list_to_string(list):
	return reduce(lambda a, b: str(a)+"\n"+str(b), list)

if __name__ == '__main__':
	print(list_to_string(["khoury", "college", "align", "masters"]))