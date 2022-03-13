import glob

#Pegar caminho completo com todos os csvs e colocar todos dentro de uma lista
path = '/home/user/...'
file = path + 'data.csv'
all_files = [i for i in glob.glob(path+ '*csv')]
fout = open(file, 'a')
for i in range(len(all_files)):
    if i == 0:
        for l in open(all_files[i]):
            fout.write(l)
        else:
            f = open(all_files[i])
            next(f)
            for k in f:
                fout.write(k)
            f.close()
fout.close()