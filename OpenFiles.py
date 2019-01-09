
import os
failedFiles=[]
sucessFiles=[]
for root, dirs, files in os.walk("/media/sf_cdrive/emailClicks/"):  
    for filename in files:
        try:
            
            fname = '/media/sf_cdrive/emailClicks/' + filename
            print(fname)
            cFile = pd.read_csv(fname, error_bad_lines = True,delimiter='|',header=0,encoding='unicode-escape')
        except:
            print('Can not open: ' + filename)
