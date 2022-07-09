vagas = {'Analista de Dados': ['python', 'power bi', 'sql', 'boa comunicação'],
         'Cientista de Dados': ['python', 'banco de dados', 'machine learning']}
inscritos = dict()


# nome_arquivo = input('Insira o nome do arquivo que contém o currículo do candidato (insira o path se necessário): ')
# nome_candidato = input('Qual o nome do candidato? ')
# cv = open(nome_arquivo, 'r')
numCandidatos = int(input('Quantos candidatos serão inscritos? '))


def listarInscritos(inscritos):
    cont = 0
    while cont < numCandidatos:
        nome_arquivo = input(
            'Insira o nome do arquivo que contém o currículo do candidato (insira o path se necessário): ')
        nome_candidato = input('Qual o nome do candidato? ')
        novaInscricao = {nome_candidato: nome_arquivo}
        inscritos.update(novaInscricao)
        cont = cont + 1
    
    return inscritos


def avaliarCurriculo(cv, vagas):
    termoSeEncaixa = []
    texto = cv.read()
    for vaga in vagas:
        for termo in vagas[vaga]:
            if termo in texto:
                termoSeEncaixa.append(vaga)

    aptoPara = []
    for i in termoSeEncaixa:
        if i not in aptoPara:
            aptoPara.append(i)

    return aptoPara


def aprovaCandidatos(inscritos):
    for candidato in inscritos:
        cv = open(inscritos[candidato])
        aptoPara = avaliarCurriculo(cv, vagas)
        if len(aptoPara) == 0:
            return(f'O candidato {candidato} não está apto para nenhuma vaga')
        else:
            for i in aptoPara:
                print(f'O candidato {candidato} está apto para a vaga de {i}')


#
listarInscritos(inscritos)
aprovaCandidatos(inscritos)
