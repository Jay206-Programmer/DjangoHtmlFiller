import os

def DjangoFormatter(filepath):
    
    if filepath.endswith(".html") or filepath.endswith(".htm"):
        oldf = open(filepath, 'r')
        if not os.path.isdir("Formatter_Generated_Files"):
            os.mkdir("Formatter_Generated_Files")
        newfile = open(f'Formatter_Generated_Files\{filepath}', 'w')
        strng = oldf.readlines()
        count = 0

        print(f"\n###Formatter Started for {filepath}...")

        newfile.write("{% load static %}\n")

        for line in strng:
            if 'href' in line and '{%' not in line and '#' not in line:
                hrefind = line.find('href') +4
                start_ind = line.find('"',hrefind) +1
                line = line[:start_ind]+"{% static '"+line[start_ind:]

                end_ind =  line.find('"',start_ind)
                line = line[:end_ind]+"' %}"+line[end_ind:]

                count+=1

            if 'src' in line and '{%' not in line:
                hrefind = line.find('src') +4
                start_ind = line.find('"',hrefind) +1
                line = line[:start_ind]+"{% static '"+line[start_ind:]

                end_ind =  line.find('"',start_ind)
                line = line[:end_ind]+"' %}"+line[end_ind:]

                count+=1    

            newfile.write(line)    
        else:
            print(f"Execution compleate, {count} changes made in file {filepath}\n")
            oldf.close()
            newfile.close()
            
                    