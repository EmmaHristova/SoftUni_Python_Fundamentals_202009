# 08-02. TEXT PROCESSING [Exercise]
# 03. Extract File

path = input()

file_name_start = path.rfind('\\') + 1
file_name_end = path.rfind('.')

file_name = path[file_name_start:file_name_end]
file_extension = path[file_name_end+1:]

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')
