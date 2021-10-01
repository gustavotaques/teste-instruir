# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

## O problema

A equipe de desenvolvimento _Bleeding Edge Enthusiasts_ (BEE) se orgulha de 
usar as tecnologias mais recentes e modernas. Essa regra também se aplica aos
projetos desenvolvidos em Python pela equipe BEE.

Para garantir que todos seus projetos em Python estão usando as últimas versões
disponíves dos pacotes, a equipe pensou em criar uma ferramenta batizada de 
MagPy. A ferramenta recebe um nome de projeto, uma lista de pacotes e devolve a 
última versão de cada pacote.

Um dos integrantes da BEE apontou que a 
[API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html)
poderia ser usada para esse fim.

## Solução

Você deve desenvolver a MagPy, uma API REST que gerencia uma coleção de 
projetos. Cada projeto tem um nome e uma lista de pacotes. Cada pacote tem um 
nome e uma versão.

O cadastro de um projeto recebe o nome e a lista de pacotes. Cada pacote da 
lista precisa obrigatoriamente especificar um nome, mas a versão é opcional.

Sua API deve validar o projeto cadastrado: todos os pacotes informados devem
estar cadastrados no [PyPI](https://pypi.org/). Portanto você deve verificar o
nome e a versão do pacote.

Quando o pacote vem apenas com o nome, sua API deve assumir que é preciso usar
a última versão publicada no [PyPI](https://pypi.org/).

Abaixo, alguns exemplos de chamadas que serão feitas nessa API:

```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "Django"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```
O código HTTP de retorno deve ser 201 e o corpo esperado na resposta é:
```
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},  // Usou a versão mais recente
        {"name": "graphene", "version": "2.0"}   // Manteve a versão especificada
    ]
}
```

Se um dos pacotes informados não existir, ou uma das versões especificadas for
inválida, um erro deve ser retornado.

Para uma chamada semelhante ao exemplo abaixo:
```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "pypypypypypypypypypypy"},
        {"name": "graphene", "version": "1900"}
    ]
}
```
O código HTTP de retorno deve ser 400 e o corpo esperado na resposta é:
```
{
    "error": "One or more packages doesn't exist"
}
```

Também deve ser possível visitar projetos previamente cadastrados, usando o
nome na URL:
```
GET /api/projects/titan
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```

E deletar projetos pelo nome:
```
DELETE /api/projects/titan
```

| ⚠️ | Sua solução deve usar a [API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html). Não use outro caminho pra buscar as informações necessárias |
| --- | --- |


## Avaliação

Os testes básicos estão disponíveis neste repositório no arquivo
`tests-open.js`. Use-os durante o desenvolvimento para avaliar se a sua API 
está correta. Como explicado acima, você **não passará** para a próxima etapa 
se a sua solução não atender todos os testes desse arquivo. 
**Use os testes para guiar o desenvolvimento da solução.**

Você pode executar esses testes com o [k6](https://k6.io/). Para instalar o k6
basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu
sistema operacional (Windows, Linux ou Mac).

Para rodar os testes abertos, especifique a variável de ambiente "API_BASE"
com o endereço base da API testada.

Exemplo de aplicação rodando no localhost na porta 8000:
```
k6 run -e API_BASE='http://localhost:8000/' tests-open.js
```
## Recomendações finais

- Não deixe para fazer na última hora
- [Não teste apenas o _Happy Path_](https://cucumber.io/blog/test-automation/happy-unhappy-paths-why-you-need-to-test-both/)

**Boa sorte!**
