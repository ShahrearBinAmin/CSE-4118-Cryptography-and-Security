good_file=open('good.txt').read()
bad_file=open('evil.txt').read()

for i in range(len(good_file)):
    if(good_file[i]!=bad_file[i]):
        print i,good_file[i],bad_file[i]