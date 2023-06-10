from glob import glob
import os
import platform
import re
from cleanupdict import replaces

# print(platform.system()) # 'Windows' # For Linux it prints 'Linux'. For Mac, it prints `'Darwin'
# print(os.name) #posix or nt, then use os.name.


#in_folder = r'hc-srt' 
in_folder = r'test' 
out_folder = r'hc-srt' 


def cleanup():
    osname = platform.system()

    os.chdir(in_folder)
    my_files = glob('*.srt')
    # print(my_files)

    for file in my_files: 
        # print(file)
        # print(os.path.abspath(file))
        # file = os.path.abspath(file) # os.chdir(in_folder) make you in this folder, if you just work in this folder, you don't need this
        count = 0
        with open(file, 'r', encoding="utf8") as fi: 
            file_out = 'o-' + file   # in the same folder as in_folder 
            # print(file)
            # print(file_out)
            with open(file_out, 'a+', encoding="utf8") as fo:
                for line in fi.readlines():  
                    # line = line.strip() # keep empty line
                    for rep in replaces:
                        if rep in line:
                            line = re.sub(rep, replaces[rep], line) # remove spaces 
                            count = count + 1

                    fo.write(line )

        print('{} has {} changes.'.format(file, count))

if __name__ == '__main__':
   cleanup()
   print('finished')    
    
