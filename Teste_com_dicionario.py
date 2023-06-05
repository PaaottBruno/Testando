#exemplo dado nas minhas pesquisas

dados = {'nome':['Bruno'],'idade':[17]}     #dicionario, nome esta no indice 'nome' e 'idade' tambem, 
# como se fosse uma lista mas no lugar do indece 0,1... ele esta armazenado em dados no indice 'nome' e 'idade'
print(dados['nome'])        #aqui esta sendo printado o indece 'nome'
print(dados['idade'])       # aaqui esta sendo printado o indece 'idade'

                    #append não funcina em dicionaio
dados['sexo'] = 'M' # Aqui esta adicionando um indice 'sexo' e esta armazenando 'M'

print(dados.values())  # os valores, exem: Bruno, 17, M
print(dados.keys())     # As cheves/keys, Exem: nome, idade, sexo
print(dados.items())       # os Itens, Exem: ('nome', ['Bruno']),  ('idade', [17]),  ('sexo', 'M')


for k,v in dados.items():  # for vai repetir quantas vezes tiver 'elementos para ser lidos'
    print(f"O {k} é {v}")       # printando as keys e values, k e v ou chave e valor.