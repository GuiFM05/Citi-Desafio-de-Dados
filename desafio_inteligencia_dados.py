import pandas as pd

# Definir o ID do arquivo e o gid
file_id = '1h03wpzXorKvd_rjP_2eOBj0q6Bm80gYi8nyinmawXsU'
gid = '205418271'
url = f'https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv&gid={gid}'
dataframe = pd.read_csv(url)

# 1. Padronizar a coluna Sexo:
sexo_adequado = {
    "fem" : "Feminino",
    "F" : "Feminino",
    "Feminino" : "Feminino",
    "M" : "Masculino",
    "masc" : "Masculino",
    "Masculino" : "Masculino"
}
dataframe['sexo'] = dataframe['sexo'].map(sexo_adequado)

# 2. Converter notas para float
dataframe['nota_matematica'] = dataframe['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
dataframe['nota_portugues'] = dataframe['nota_portugues'].astype(str).str.replace(',', '.').astype(float)

# 3. Calcular média
dataframe['media'] = (dataframe['nota_matematica'] + dataframe['nota_portugues'] + (dataframe['frequencia'] / 10)) / 3

# 4. Verificar aprovação
dataframe['aprovado'] = dataframe['media'].apply(lambda x: 'Sim' if x >= 7 else 'Não')

# 5. Converter de volta para visualização com vírgula
dataframe['nota_matematica'] = dataframe['nota_matematica'].apply(lambda x: str(x).replace('.', ','))
dataframe['nota_portugues'] = dataframe['nota_portugues'].apply(lambda x: str(x).replace('.', ','))
dataframe['media'] = dataframe['media'].round(2).apply(lambda x: str(x).replace('.', ','))

# 6. Exportar para Excel
dataframe.to_excel("alunos_avaliados.xlsx", index=False)
