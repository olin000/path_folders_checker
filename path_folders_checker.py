import os

path = os.environ['PATH']
path_list = path.split(os.pathsep)

for entry in path_list:
    if not os.path.isdir(entry):
        print(entry)
