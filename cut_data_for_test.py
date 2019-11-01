import pandas as pd


def main():
    path = "C:\\test_formats\\"
    #file = "MItoMI-2013-12-20.txt" #file of size 6.86GB
    file = "MItoMI-2013-12-26.txt"  # file of size 2.88GB
    wfile = open("test_file_small.txt", 'w')
    with open(path+file, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            wfile.write(line)
            i+=1
            if i==10000:
                break

    wfile.close()







if __name__=='__main__':
    main()