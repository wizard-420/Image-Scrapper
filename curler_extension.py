import os
import requests as rq
import re

#p = input("Enter the string pattern you want to grep: ")
#search_catagory = input("Enter your search category")
def process():
    f = open("result.txt","r")
    i=1
    parent = input("Enter main category: ")
    child = input("Enter sub-category: ")
    path = "image_dump/"
    try:
        os.mkdir(path+parent)
    except:
        print("Directory already exists")
    finally:
        path = path+parent+"/"
        print("current downloading path: ",path)


    try:
        os.mkdir(path+child)
    except:
        print("Directory already exists")
    finally:
        path = path+child+"/"
        print("current downloading path: ",path)
    while True:
        l = f.readline()  
        try:
            img = rq.get(l).content
            with open(path+str(i)+".jpeg","wb+") as fi:
                fi.write(img)
            print("downloaded image no. ",i)
        except:
            print("Error while fetching")
            break
        finally:
            if(i>50):
                f.close()
                break
            i+=1 

if __name__=="__main__":
    process()
