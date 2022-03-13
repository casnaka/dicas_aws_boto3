import glob


path = '/home/user/...'
file = path + 'data.csv'
#Pegar caminho completo com todos os csvs e colocar todos dentro de uma lista
all_files = [i for i in glob.glob(path+ '*csv')]
#Criando o arquivo que vai receber todos os os dados 
fout = open(file, 'a')
for i in range(len(all_files)):
    #condicao criada caso o arquivo tenha header e precisa ser ignorado apos o segundo arquivo
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