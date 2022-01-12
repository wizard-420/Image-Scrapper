import curler_extension

def filter():
    f= open("result.txt","r")
    fc=f.read()
    print(fc)
    curler_extension.process()

if __name__=="__main__":
    filter()