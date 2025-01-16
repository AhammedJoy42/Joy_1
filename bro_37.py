
#Open & Copy file
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation & modification times)

try:
    import shutil

    shutil.copyfile('test.txe', 'copy.txt');   #(source, destination)

except FileNotFoundError:
    print("Something is wrong");