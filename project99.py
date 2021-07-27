import os, shutil

path=input('Enter path :- ')
timereq=((30*24)*60)*60

exist=os.path.exists(path) 
if exist==True:
    print('')
else:
    print('Path not found')

func=input('Is the path to a file? (y/n) :- ')
if func=='n':
    files = os.listdir(path)
    new_path=os.path.join(path,files[0])
else:
    new_path=path

time=os.stat(new_path).st_ctime
print(time)
print(timereq)

def delete():
    if func=='y':
        os.remove(new_path)
    else:
        shutil.rmtree(new_path) 

if time>timereq:
    delete()
else:
    print('File/Folder is not that old.')