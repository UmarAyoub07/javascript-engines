import os
import zipfile

def create_package(exe_list, package_name):
    with zipfile.ZipFile(package_name, 'w') as zipf:
        for file in exe_list:
            if os.path.isfile(file):
                zipf.write(file)
            else:
                print(f"{file} does not exist!")
                
def main():
    exe_list = input("Enter the names of the executable files separated by a comma: ").split(',')
    package_name = input("Enter the name of the package: ")
    create_package(exe_list, package_name + ".zip")

if __name__ == "__main__":
    main()