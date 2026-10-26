# SITE ANIVERSÁRIO ALANNA MEU AMOR DA MINHA VIDA <3
    # comando execução:
    # python -m streamlit run main.py

# TELA INICIAL
    # TÍTULO -> FELIZ ANIVEERSÁRIO ALANNA <3
    # FORMATO CORAÇÃO
    # TEXTO DE FELIZ ANIVERSÁRIO
    # FOTOS NOSSAS SE O STREAMLIT PERMITIR

# IMPORTAÇÃO DAS BIBLIOTECAS
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# 3H28 VAI TOMANDOOO LULA PRO MAX 2027 E MEU AMOR 19 ANOS!!!
# AGORA TOCANDO 'Primavera - Tim Maia'
    # Quando o inverno chegar, eu quero estar junto a ti, quando o outono chegar, eu quero estar junto a ti, porque é primavera... Porque te amooo...


# FUNCAO FORMATO DO CORACAO
    # AGORA TOCANDO "Since I've Been Loving You" - Led Zeppelin
    # SÃO 3 DA MANHÃ, E EU AMO VOCÊ, FELIZ ANIVERSÁRIO <3
t = np.linspace(0, 2 * np.pi, 500)
x = 16 * np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# PLOTLY FIGURA CORACAO
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines",
    line=dict(color="red", width=4),
    fill="toself"
))

fig.update_layout(
    width=600,
    height=600,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=0, r=0, t=0, b=0)
)

# MOSTRA DENTRO DO STREAMLIT
# TITULO
st.markdown(
"<h1 style='text-align: center; color: black;'>FELIZ ANIVERSÁRIO AMOR</h1>",
unsafe_allow_html=True
)

# CORACAO PLOTLY
st.plotly_chart(fig, use_container_width=True)

paragrafo = st.container(border=True)
paragrafo.markdown(
"<h2 style='text-align: justify; color: black;'>VOCÊ É A DATA DE HOJE? <br>"
"Porque você é 26/10!!! </h2><br>"
"<h3 style='text-align: justify; color: black;'>Brincadeiras a parte, eu espero que seu dia tenha sido bom e que você aproveite ainda mais. Você já sabe que te quero muito, mas sempre é um prazer dizer, ou escrever, que te amo. <br>"
"Lembra de quando a gente estava lá na Lapa com os belgas, e eu te disse para prestar atenção na música de fundo? Pois, é... <br>"
"Estou ouvindo essa música agora, é a São Gonçalo do Seu Jorge, mas no momento que tocou, era para reparar no início apenas kkk, que fala: <br>"
"<p style='text-align: center; color: black;'><br>Pretinha, faço tudo pelo nosso amor, <br>" \
"Faço tudo pelo bem do nosso bem, meu bem, <br>" \
"A saudade é minha dor, e anda arrasando com o meu coração <br>" \
"E não duvide que um dia eu te darei o céu, <br>" \
"O meu amor junto com um anel, pra gente se casar <br>" \
"No cartório ou na igreja. </p><br> " \
"Agora está tocando 'Eternamente - Gal Costa', e são 3h46 da madrugada... Eu amo você, minha linda. Sabe de uma coisa? Em busca de palavras para escrever agora, eu busquei aquele código que escrevi para ti uns meses atrás, <br>"
"e reparei que aindo sinto as mesmas coisas que senti na Quinta da Boa Vista quando você disse que me ama pela primeira vez, e participar de um aniversário seu é algo muito especial. <br>" \
"Se eu dissesse para o Giovani de janeiro que agora eu estaria namorando (e ainda mais que seria com você, e que seria tão incrível assim), acho que eu me acharia louco... Mas, como Gal Costa diz: <br>"
"<p style='text-align: center; color: black;'><br>Vou ter sempre você comigo, <br>"
"Nosso amor eu canto e cantarei, <br>"
"Você é tudo o que eu amei na vida, <br>"
"Nunca vou te esquecer, <br>"
"Só mesmo o tempo pode revelar, <br>"
"O lado oculto das paixões, "
"O que se foi e o que não passará, <br>"
"Inesquecíveis sensações, <br>"
"Que sempre vão ficar, <br>"
"Pra nos fazer lembrar, <br>"
"Dos sonhos, beijos, <br>"
"Tantos momentos bons. </p><br><br>"
"Enfim, eu não sei muito bem o que falar além do que já disse aqui, e to ficando com sono também, pois são mais de 4h da manhã já e ainda estou escrevendo o código, mas te amo e espero que seu dia seja maravilhoso! <br></h3>"
"<h4 style='text-align: center; color: black;'>Eu amo você, minha linda.<br>"
"Feliz aniversário! </h4>",
unsafe_allow_html=True
)
