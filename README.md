# DjangoHtmlFiller

This code is for those who are tired of inserting `{% static ' ' %}` in every **href,src** links in __*html*__ files while creating a __*Django project*__. :sassy_man:

_From this:_

![Normal Html](/Images/Normal.png)

_To this:_ 

![Formatted for Django](/Images/AfterExec.png)

## Purpose:
- The Main puspose of this code is to **save hours of work** by **_automatically_** scanning through  & updating all the _html_ files in the given folder.
- It will store all the _updated files_ in a __seperate folder__ in the same directory **_without_ harming** the _original files_.
  - You can **_examine & finalize_** all the changes and then __`cut+paste`__ those files in place of _original files_ later on. 
  - You **_won't lose_** any of _your files_.
- This code is _properly tested_ & works **_100%_** of the time. :heavy_check_mark:

## How To Use:
#### 1. Through Github:
Steps:
1. __Clone__ this _repository_ **anywhere** in your pc. (**No need** to clone in your _Django project_ folder!)
2. Now do __`cd (Cloned Directory path)/DjangoHtmlFiller/OsScrawler.py`__ and then _run_ __`OsScrawler.py`__ program. 

   ![Run Code](/Images/Run.png)
  
3. Now the _program_ will ask for the _**folder**_ in which all your _**html/htm** files_ are stored. In this _example_ all of _Django Project's **html** files_ are stored in _**templates** folder_.

   ![Assets Folder](/Images/Folder.png)
   
- You can give _the program **full path**_ of that **folder** (**_all_** the **html** files within that _folder_ will be **_scanned_**) _or_ you can _**directly**_ give the _path_ of the *__html__ file* you want to _scan & update_ (_**only**_ _that file_ will be _scanned_).  
- In this case I am _giving path_ of the **templates** folder in which _all_ of the _**html**_ files are stored.

   ![Give Full Path](/Images/GivingFilePath.png)
   
- The _program_ will _scan through_ given _**html** file(s)_ & will save converted outputs in _**Formatter_Generated_Files** folder_ in the **same** _directory_.

   ![program Execution](/Images/Execution.png)
  
   ![Run Code](/Images/NewFolder.png)
