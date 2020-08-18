import os
import sys
import Inserter


def indent(num):
    return "\t"*num

def Scrawler(t=0):
    list = os.listdir()

    for dir in list:
        if os.path.isdir(dir):
            t += 1
            print(indent(t)+f"*****Entering Folder {dir}*****")
            os.chdir(dir)
            t = Scrawler(t)
        else:
            print(indent(t)+"-> "+dir)
            
    print(indent(t)+f"*****Exiting Folder {os.path.basename(os.getcwd())}*****")        
    t -= 1
    os.chdir("..")
    return t

def Finder(key,finds):
    list = os.listdir()
    
    for dir in list:
        if key in dir:
            finds.append(os.getcwd()+"\\" +dir)
            
        if os.path.isdir(dir):
            os.chdir(dir)
            finds = Finder(key,finds)        
            
    os.chdir("..")
    return finds


def Scrawl_Folder():
    try:
        fld = input('Enter the folder you want to Scrawl: ')
        if fld == "quit()":
            sys.exit()       
        print(f"\n*****Entering Folder {fld}*****")
        os.chdir(fld)
        Scrawler()
    except:
        print(sys.exc_info()[0],"Occured!")
        
def Findin_Folder():
    try:
        finds = list()    
        fld = input('Enter the folder you want to Scrawl: ')
        print(f"\n*****Entering Folder {fld}*****")
        os.chdir(fld)
        print("FINDING...")

        A = Finder(input("Key: "),finds)            
        if len(A) == 0:
            print("No Match Found!!")
        else:
            print(f"{len(A)} results found:")
            for i in A:
                print(i)
    except:
        print(sys.exc_info()[0],"Occured!")        

def DjangoScrawler():
    list = os.listdir()
    for dir in list:
        if os.path.isdir(dir) and dir != "Formatter_Generated_Files":
            print(f"*****Entering Folder {dir}*****")
            os.chdir(dir)
            DjangoScrawler()
        else:
            if dir.endswith(".html") or dir.endswith(".htm"):
                Inserter.DjangoFormatter(dir)
                
            
    print(f"*****Exiting Folder {os.path.basename(os.getcwd())}*****")        
    os.chdir("..")

def DjangoBot():
    try:
        fld = input('Enter the folder you want to Scrawl: ')
        if os.path.isdir(fld):
            print(f"\n*****Entering Folder {fld}*****")
            os.chdir(fld)
            DjangoScrawler()
        else:
            if fld.endswith(".html") or fld.endswith(".htm"):
                Inserter.DjangoFormatter(fld)
            else:
                print("Error, Given file type is unsupported!! Please give only .html or .htm file path to the formatter.")                    
                
    except:
        print(sys.exc_info()[0],"Occured!")
    

if __name__ == '__main__':
    DjangoBot()
    