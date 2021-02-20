import os

print('Hello World!')

print('I just entered the branch \'develop\'')

x = 1

if -1 != x:
    print('Neni rovno!!!')

print('Nachazim se v novem developu, ten stary uz jsem smazal!')

print('Neco jsem dodelat, ale jeste nepridal')

folder = 'C:/Users/Vojta/Documents/git/repo-try-out'
files_dirs = os.listdir(folder)
print(files_dirs)

for file_dir in range(len(files_dirs)):
    if not os.path.isdir(os.path.join(folder, str(file_dir))):
        print('Je to file!')
    else:
        print('Neni to file, je to folder!')