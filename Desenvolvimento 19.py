import enum

class Eleicao(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0

def votacao():
    votos_X = 0
    votos_Y = 0
    votos_Z = 0
    brancos = 0
    nulos = 0
    sair = 2
    total_votos = 0
    vencedor = []
    votos = 0
    while (sair == 2):
        try:
            voto = int(input("\n Digite seu voto:\n - candidato X => 889\n - candidato Y => 847\n - candidato Z => 515\n - branco => 0\n"))
            finalizar = int(input("\n Se deseja finalizar a votação digite: \n 1 - Sim \n 2 - Não \n"))
            while ((finalizar !=1) and (finalizar!=2)):
                finalizar = int(input("Se deseja finalizar a votação digite: \n 1 - Sim \n 2 - Não \n"))
            sair = finalizar
            if voto == Eleicao.candidato_X.value:
                votos_X = votos_X + 1
            elif voto == Eleicao.candidato_Y.value:
                votos_Y = votos_Y + 1
            elif voto == Eleicao.candidato_Z.value:
                votos_Z = votos_Z + 1
            elif voto == Eleicao.branco.value:
                brancos = brancos +1
            else:
                nulos = nulos +1

        except:
            print("Erro, tente novamente!")
        total_votos = total_votos + 1
    if (votos_X > votos_Y) and (votos_X > votos_Z):
        vencedor = Eleicao.candidato_X.name
        votos = votos_X
    elif (votos_Y > votos_X) and (votos_Y > votos_Z):
        vencedor = Eleicao.candidato_Y.name
        votos = votos_Y
    elif (votos_Z > votos_X) and (votos_Z > votos_Y):
        vencedor = Eleicao.candidato_Z.name
        votos = votos_Z
    
    print("O vencedor foi ",vencedor)
    print("O Candidado X recebeu",votos_X,"votos")
    print("O Candidado Y recebeu",votos_Y,"votos")
    print("O Candidado Z recebeu",votos_Z,"votos")
    print("Foram",brancos,"votos brancos")
    print("Foram",nulos,"votos nulos")
    

votacao()


    

        