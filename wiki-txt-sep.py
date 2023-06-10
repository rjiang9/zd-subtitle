import glob
import os
import platform
import re

# print(platform.system()) # 'Windows' # For Linux it prints 'Linux'. For Mac, it prints `'Darwin'
# print(os.name) #posix or nt, then use os.name.


def main():
    osname = platform.system()

    lbk = ''

    if osname == 'Windows':
        lbk = '\r\n'
    elif osname == 'Linux':
        lbk = '\n'
    elif osname == 'Darwin':
        lbk = '\n'


    print(lbk)


    """ 
    For Windows, it is CRLF (\r\n)
    For UNIX, it is LF (\n)
    For MAC (up through version 9) it was CR
    For MAC OS X, it is LF
    """

    os.chdir(r'txt')
    my_files = glob.glob('*.txt')
    #print(my_files)

    for file in my_files: 

        with open(file, 'r', encoding="utf8") as fi: 
            file_out = 'o-' + file 
            with open(file_out, 'a+', encoding="utf8") as fo:
                for line in fi.readlines():  
                    line = re.sub(r"\s+", "", line) # remove spaces 
                    if line == "":
                        continue

                    newline = re.sub('[，|。|；]', lbk, line)   # replade Chinese , and . by 
                    fo.write(newline)



if __name__ == '__main__':
    main()
    
