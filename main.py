import streamlit as st
import pandas as pd
import plotly.express as px

st.title("UPS - Dezembro (03/11 - 17/12) 📋")

st.write("## Aspirantes")

aspirantes = pd.DataFrame({
    "Aspirantes": ["Voz", "Sky", "Guto", "Felipe", "Gilsão", "Follow"],
    "Curso Aplicado": [65, 15, 23, 15, 17, 31],
    "Logs Feitas": [86, 54, 14, 26, 10, 15],
})
aspirantes["Média de Cursos Aplicados"] = aspirantes["Curso Aplicado"].mean()
aspirantes["Média de Logs Feitas"] = aspirantes["Logs Feitas"].mean()

st.write(aspirantes)

st.bar_chart(aspirantes, x="Aspirantes", y="Curso Aplicado")
st.bar_chart(aspirantes, x="Aspirantes", y=("Logs Feitas"))
fig = px.pie(aspirantes, values='Logs Feitas', names='Aspirantes', title='Logs Feitas por Aspirantes')
fig2 = px.pie(aspirantes, values='Curso Aplicado', names='Aspirantes', title='Cursos Aplicados por Aspirantes')

st.plotly_chart(fig)
st.plotly_chart(fig2)

st.write("## Capitães")

capitaes = pd.DataFrame({
    "Capitães": ["Godoy", "Menom", "Isaac", "Taki"],
    "Curso Aplicado": [0, 16, 51, 16],
    "Logs Feitas": [16, 81, 18, 7],
})

capitaes["Média de Cursos Aplicados"] = capitaes["Curso Aplicado"].mean()
capitaes["Média de Logs Feitas"] = capitaes["Logs Feitas"].mean()

st.write(capitaes)

st.bar_chart(capitaes, x="Capitães", y="Curso Aplicado")
st.bar_chart(capitaes, x="Capitães", y=("Logs Feitas"))
ct_pie = px.pie(capitaes, values='Logs Feitas', names='Capitães', title='Logs Feitas por Capitães')
ct_pie2 = px.pie(capitaes, values='Curso Aplicado', names='Capitães', title='Cursos Aplicados por Capitães')

st.plotly_chart(ct_pie)
st.plotly_chart(ct_pie2)

st.write("## Majores")

majores = pd.DataFrame({
    "Majores": ["Guh", "Noltz", "Marcelo", "Steve", "Demura"], # "Pepino", "Lucas Paiva"],
    "Curso Aplicado": [0, 25, 4, 12, 13],
    "Logs Feitas": [0, 19, 0, 0, 90],
    "Set DC Fluxo": [0, 45, 1, 4, 195]
})

majores["Média de Cursos Aplicados"] = majores["Curso Aplicado"].mean()
majores["Média de Logs Feitas"] = majores["Logs Feitas"].mean()
majores["Média de Set DC Fluxo"] = majores["Set DC Fluxo"].mean()

st.write(majores)
st.write("""
*Noltz: Upou dia 01/10
         
*Marcelo: Upou dia 17/09
""")

st.bar_chart(majores, x="Majores", y="Curso Aplicado")
st.bar_chart(majores, x="Majores", y=("Logs Feitas"))
mj_pie = px.pie(majores, values='Logs Feitas', names='Majores', title='Logs Feitas por Majores')
mj_pie2 = px.pie(majores, values='Curso Aplicado', names='Majores', title='Cursos Aplicados por Majores')
mj_pie3 = px.pie(majores, values='Set DC Fluxo', names='Majores', title='Set DC Fluxo por Majores')

st.plotly_chart(mj_pie)
st.plotly_chart(mj_pie2)
st.plotly_chart(mj_pie3)

st.write("## Tenente Coronel")

tenente_coronel = pd.DataFrame({
    "Tenente Coronel": ["Pepino"],
    "Curso Aplicado": [10],
    "Logs Feitas": [5],
    "Set DC Fluxo": [61]
})