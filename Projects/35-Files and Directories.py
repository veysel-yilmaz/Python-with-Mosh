# Absolute path, 2 examples are below
# c:\Program Files\Microsoft
# /usr/local/bin --> on Mac

# Relative path, which we will use here

from pathlib import Path

path = Path("ecommerce")
print(path.exists()) #is supposed to return true boolean value

"""path = Path("emails")
# print(path.mkdir())
path = Path("ecommerce")
print(path.rmdir())"""

path = Path()
# print(path.glob('*.*')) for searching everthing
#print(path.glob('*.py'))
# for all the files and directories write glob('*')
for file in path.glob('*.py'):
    print(file)
