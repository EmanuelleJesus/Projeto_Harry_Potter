import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"
st.set_page_config(layout='wide')
# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()

# Pega apenas os nomes dos personagens , a partir de uma lista vazia
nomes = []
for personagem in dados:
    nomes.append(personagem['name'])


# Ordena os nomes em ordem alfabética
nomes.sort()




# Título do app
st.title('Hogwarts Weaslay - O lugar onde voce encontra informações do seu bruxo favorito')



# Sidebar com a lista de nomes
nome_escolhido = st.selectbox('Escolha um Bruxo', nomes)



# Procura o personagem escolhido na lista de dados
personagem = None
for p in dados:
    if p ['name'] == nome_escolhido:
     personagem = p 
     break



# Mostra o nome do personagem
st.header(f'Nome do personagem {personagem['name']}')



# ===== IMAGEM EM DESTAQUE =====
# Verifica se o personagem tem imagem
if personagem['image'] and personagem['image'] !="":
   st.image(personagem['image'], width=300)
else:
   st.write("este personagem não possui imagem")

# Linha divisória
st.divider()

# Informações principais
st.write(f"**Casa:** {personagem['house']}")
st.write(f"**Espécie:**{personagem['species']}")
st.write(f"**Gênero:**{personagem['gender']}")
st.write(f"**Data de Nascimento:**{personagem['dateOfBirth']}")
st.write(f"**Ano de Nascimento:**{personagem['yearOfBirth']}")
# Informações da varinha
st.write("**Varinha:**")
st.write(f"- Madeira: {personagem['wand']['wood']}")
st.write(f"- Núcleo: {personagem['wand']['core']}")
st.write(f"- Tamanho: {personagem['wand']['length']} polegadas")


st.write(f"**Patrono:** {personagem['patronus']}")
st.write(f"**Ator/Atriz:** {personagem['actor']}")                                                                      




# Mostra se está vivo

