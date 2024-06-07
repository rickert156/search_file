import os

class SearchFiles:

	def searchCSV():
		search_files = os.listdir()
		list_dirs = []
		for search_file in search_files:
		    if '.csv' in search_file:list_dirs += [search_file]

		num=0
		for list_dir in list_dirs:
		    num+=1
		    print(f'[{num}] {list_dir}')

		enter_list = int(input('[x] Введите значение: '))
		enter_list-=1
		document = (list_dirs[enter_list])
		print(f'[x] {document}')
