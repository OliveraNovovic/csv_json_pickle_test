import pandas as pd
import pyarrow.parquet

def main():
    path = "C:\\test_formats\\"
    fpath = "D:\\Documents_old\\Milano_data\\MItoMI\\December_2013_full\\full\\"
    file = fpath + "MItoMI-2013-12-20.txt" #file of size 6.86GB
    #file = "test_file_small.txt" #test file with just 10 000 lines
    data = pd.read_csv(file, sep='\t', names=["timestamp", "sqid1", "sqid2", "weight"]) #parquet writer will ask for string header
    #print(data.head(5))

    #data.to_pickle(path + 'MItoMI-2013-12-20.pkl')
    #data.to_json(path + 'MItoMI-2013-12-20.json')
    data.to_parquet(path + 'MItoMI-2013-12-20.parquet', compression=None)

    #compressed versions
    #data.to_pickle(path + 'MItoMI-2013-12-20_compress.pkl', compression='gzip')
    #data.to_json(path + 'MItoMI-2013-12-20_compress.json', compression='gzip')
    data.to_parquet(path + 'MItoMI-2013-12-20_compress.parquet.gzip', compression='gzip')




if __name__=='__main__':
    main()
