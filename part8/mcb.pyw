
import sys, pyperclip, shelve

print(sys.argv)

shelf_file = shelve.open('mcb')

if(len(sys.argv) == 3) and sys.argv[1].lower() == 'save':
  shelf_file[sys.argv[2]] = pyperclip.paste()
elif(len(sys.argv) == 2):
  if (sys.argv[1].lower() == 'list'):
    print('\n'.join(list(shelf_file.keys())))
  elif(sys.argv[1] in shelf_file):
    print(shelf_file[sys.argv[1]])

shelf_file.close()

