vagas = {'Analista de Dados': ['python', 'power bi', 'sql', 'boa comunicação'],
         'Cientista de Dados': ['python', 'banco de dados', 'machine learning']}

inscritos = dict()

numCandidatos = int(input('Quantos candidatos serão inscritos? '))


def listarInscritos(inscritos):
    cont = 0
    while cont < numCandidatos:
        novaInscricao = dict()
        nome_arquivo = input(
            'Insira o nome do arquivo que contém o currículo do candidato (insira o path se necessário): ')
        nome_candidato = input('Qual o nome do candidato? ')
        vaga_candidato = input(
                '''Para qual vaga este candidato está se aplicando?
                Oportunidades em aberto no momento:
                1 - Analista de Dados
                2 - Cientista de Dados
                Digite a opção desejada: ''')
        if vaga_candidato == 1:
            vagaPretendida = 'Analista de Dados'
            novaInscricao = {nome_candidato: [nome_arquivo, vagaPretendida]}
            inscritos.update(novaInscricao)
        else:
            vagaPretendida = 'Cientista de Dados'
            novaInscricao = {nome_candidato: [nome_arquivo, vagaPretendida]}
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
    print(f'Foram {numCandidatos} inscritos.')
    for candidato in inscritos:
        cv = open(inscritos[candidato][0])
        vagaPretendida = str(inscritos[candidato][1])
        aptoPara = avaliarCurriculo(cv, vagas)

        if len(aptoPara) == 0:
            return(f'O candidato {candidato} não está apto para nenhuma vaga')
        else:
            for i in aptoPara:
                if str(i).lower() == vagaPretendida.lower():
                    print(
                        f'O candidato {candidato} está apto para a vaga de {i} que se inscreveu.')
                elif str(i).lower() != vagaPretendida.lower():
                    print(
                        f'O candidato {candidato} também está apto à vaga de {i}.')


listarInscritos(inscritos)
aprovaCandidatos(inscritos)
