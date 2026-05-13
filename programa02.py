nt1 = float(input("Digite a primeira nota:").replace(",", "."))
nt2 = float(input("Digite a segunda nota: ").replace(",", "."))
med = (nt1+nt2)/2
if med >= 7:
    print("O aluno foi aprovado com a nota de:{}".format(med))
elif med >= 5:
    print("O aluno ficou de recuperação final\n")
    ntRec = float(input("Digite a nota da prova de recuperação do aluno:").replace(",", "."))
    if ntRec >= 5:
        print("O aluno foi aprovado através da recuperação com a nota :{} e a media anteriror de:{}".format(ntRec,med))
    else:
        print("O aluno foi reprovado com a média de:{}".format(med))
else:
        print("O aluno foi reprovado com a média de:{}".format(med))
    
