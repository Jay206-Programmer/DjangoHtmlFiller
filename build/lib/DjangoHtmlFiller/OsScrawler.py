import os
import sys
import Inserter

class OsScrawler:
    def indent(self,num):
        return "\t"*num

    def Scrawler(self,t=0):
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

    def Finder(self,key,finds):
        list = os.listdir()
        
        for dir in list:
            if key in dir:
                finds.append(os.getcwd()+"\\" +dir)
                
            if os.path.isdir(dir):
                os.chdir(dir)
                finds = Finder(key,finds)        
                
        os.chdir("..")
        return finds


    def Scrawl_Folder(self):
        try:
            fld = input('Enter the folder you want to Scrawl: ')
            if fld == "quit()":
                sys.exit()       
            print(f"\n*****Entering Folder {fld}*****")
            os.chdir(fld)
            Scrawler()
        except:
            print(sys.exc_info()[0],"Occured!")
            
    def Findin_Folder(self):
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

    def DjangoScrawler(self):
        list = os.listdir()
        for dir in list:
            if os.path.isdir(dir):
                print(f"*****Entering Folder {dir}*****")
                os.chdir(dir)
                DjangoScrawler()
            else:
                if dir.endswith(".html") or dir.endswith(".htm"):
                    obj = Inserter.DjangoFormatter()
                    obj.DjangoFormatter(dir)
                
        print(f"*****Exiting Folder {os.path.basename(os.getcwd())}*****")        
        os.chdir("..")

    def DjangoBot(self):
        try:
            fld = input('Enter the folder you want to Scrawl: ')
            if fld == "quit()":
                sys.exit()       
            print(f"\n*****Entering Folder {fld}*****")
            os.chdir(fld)
            self.DjangoScrawler()
        except:
            print(sys.exc_info()[0],"Occured!")
        

if __name__ == '__main__':
    obj = OsScrawler()
    obj.DjangoBot()
    