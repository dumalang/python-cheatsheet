import shutil
from os import path
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    if path.exists("3.3.file.txt"):

        # Get the path to the file in the current directory
        src = path.realpath("3.3.file.txt")

        # Let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # Copy over the permissions, modification times, and other info
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        if path.exists(dst):
            # Rename file
            # os.rename(dst, "3.3.file_2.txt")

            # Put things into a Zip archive
            root_dir, tail = path.split(dst)
            shutil.make_archive("3.3.zipped", "zip", root_dir)

            # More fine-grained control over ZIP files
            with ZipFile("3.3.zipped.zip", "w") as newzip:
                newzip.write("3.3.0.file.txt")
                newzip.write("3.3.1.file.txt")

if __name__ == "__main__":
    main()
