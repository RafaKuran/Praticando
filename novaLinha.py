nome = input("Diga o nome do arquivo que deseja anexar linha ao final: ")
arquivo = open(nome, "a")
novaLinha = input("Escreva a nova linha: ")
arquiva.write(novaLinha + "\n")
arquivo.close()
