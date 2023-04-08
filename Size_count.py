import os
file_name = f"{input('Path with file:')}"
file_size = os.path.getsize(file_name)
print(f'Bytes:{file_size}')
print(f'GigaBytes:{file_size //(1024*1024)/1000}')
command = "start cmd /K echo "
for i in range(0,1):
    command += str(f'GB:{int(file_size //(1024*1024)/1000)}')
os.system(command)