# 🧙‍♂️ Projeto Personagens de Harry Potter

## 📋 Descrição do Projeto

Você foi contratado pelas **Indústrias Mateus** para desenvolver um site interativo que exiba informações sobre os personagens do mundo de Harry Potter. O site deve consumir dados de uma API pública e apresentá-los de forma organizada e visualmente atraente para os fãs da saga.

## 🎯 Objetivo

Desenvolver uma aplicação web utilizando **Streamlit** que:
- Consuma a API pública de Harry Potter
- Exiba uma lista de todos os personagens
- Permita a seleção de um personagem específico
- Mostre as informações detalhadas do personagem selecionado
- Destaque a imagem do personagem na tela

## 🚀 Tecnologias Utilizadas

- **Python** - Linguagem de programação
- **Streamlit** - Framework para criação de interfaces web
- **Requests** - Biblioteca para fazer requisições HTTP
- **API Harry Potter** - Fonte de dados dos personagens

## 📦 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/harry-potter-app.git
cd harry-potter-app
```

### 2. Crie um ambiente virtual (opcional mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install streamlit requests
```

### 4. Execute a aplicação

```bash
streamlit run app.py
```

## 📝 Estrutura do Projeto

```
harry-potter-app/
├── app.py              # Código principal da aplicação
├── README.md           # Este arquivo
└── requirements.txt    # Lista de dependências (opcional)
```

## 🔍 Funcionalidades

- ✅ Lista completa de personagens na barra lateral
- ✅ Seleção de personagem por nome
- ✅ Exibição de imagem do personagem em destaque
- ✅ Informações detalhadas:
  - Casa (Grifinória, Sonserina, etc.)
  - Espécie
  - Gênero
  - Data e ano de nascimento
  - Informações da varinha (madeira, núcleo, tamanho)
  - Patrono
  - Ator/Atriz
  - Status (vivo ou não)

## 🎓 Exercício para os Alunos

### Parte 1: Entendendo o Código

1. **Localize e explique** o que faz a linha `resposta = requests.get(url)`
2. **Identifique** onde os nomes dos personagens são extraídos da API
3. **Explique** como funciona o loop `for` que procura o personagem selecionado

### Parte 2: Desafios de Melhoria

Agora que você já entendeu o projeto base, implemente as seguintes melhorias:

1. **Adicione uma mensagem de "Carregando..."** enquanto a API está sendo acessada
2. **Crie uma funcionalidade de pesquisa** que filtre os personagens pelo nome na barra lateral
3. **Adicione informações extras** como:
   - Nomes alternativos do personagem
   - Atores alternativos
   - Se é estudante ou funcionário de Hogwarts
4. **Crie um contador** que mostre quantos personagens estão vivos vs. mortos
5. **Melhore o visual** adicionando cores diferentes para cada casa de Hogwarts

### Parte 3: Desafio Avançado

**Crie uma nova funcionalidade:** Na barra lateral, além de selecionar um personagem, adicione um filtro por "casa" que mostre apenas os personagens da casa selecionada.

## 📚 Dicas para os Alunos

### Comandos Úteis do Streamlit

```python
st.title()      # Título principal
st.header()     # Subtítulo
st.write()      # Texto simples
st.image()      # Exibir imagem
st.selectbox()  # Menu de seleção
st.divider()    # Linha divisória
st.sidebar      # Barra lateral
```

### Estrutura da API

A API retorna um array de objetos com a seguinte estrutura:

```json
{
  "name": "Harry Potter",
  "house": "Gryffindor",
  "species": "human",
  "gender": "male",
  "dateOfBirth": "31-07-1980",
  "yearOfBirth": 1980,
  "wand": {
    "wood": "holly",
    "core": "phoenix tail feather",
    "length": 11
  },
  "patronus": "stag",
  "actor": "Daniel Radcliffe",
  "alive": true,
  "image": "https://ik.imagekit.io/hpapi/harry.jpg"
}
```

### Tratamento de Dados Vazios

Alguns personagens podem ter informações faltando. Use:
- `personagem.get('campo', 'Valor padrão')`
- Verificações com `if` antes de exibir

## 🎨 Exemplo Visual

Ao executar o projeto, você verá:

```
⚡ Personagens de Harry Potter

[Sidebar]  📚 Escolha um personagem
           [Harry Potter ▼]

✨ Harry Potter

[Imagem do Harry Potter em destaque]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Casa: Gryffindor
Espécie: human
Gênero: male
Data de Nascimento: 31-07-1980
Ano de Nascimento: 1980

Varinha:
- Madeira: holly
- Núcleo: phoenix tail feather
- Tamanho: 11 polegadas

Patrono: stag
Ator/Atriz: Daniel Radcliffe
Está vivo? Sim
```

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é para fins educacionais. Todos os direitos dos personagens são da J.K. Rowling e Warner Bros.

## 🧙‍♂️ Boa Sorte, Bruxos!

Divirtam-se desenvolvendo e lembrem-se: a magia está no código! ⚡
