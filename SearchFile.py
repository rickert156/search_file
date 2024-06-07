import os

class SearchFiles:

	def searchCSV():
		file_type = input('Введите тип файла(по умолчанию будет поиск по csv): ')
		search_files = os.listdir()
		list_dirs = []
		for search_file in search_files:
		    if f'.{file_type}' in search_file:list_dirs += [search_file]
		    if file_type == ' ' or file_type == '': file_type = 'csv'

		num=0
		for list_dir in list_dirs:
		    num+=1
		    print(f'[{num}] {list_dir}')

		enter_list = int(input('[x] Введите значение: '))
		enter_list-=1
		document = (list_dirs[enter_list])
		print(f'\n[x] {document}')
