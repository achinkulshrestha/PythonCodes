import sys
file = open('hexdump.txt', 'r')
while 1:
    char = file.read(2)          # read by character
    if not char: break
    sys.stdout.write('\\x')
    sys.stdout.write(char)

file.close()
