import pandas as pd
import plotly.express as px
import time

# Importando a base de dados
telecom = pd.read_csv('telecom_users.csv')
print(telecom)
print('\n')

# Tratando dados que não serão usados
telecom = telecom.drop(['Unnamed: 0'], axis=1)
print(telecom)
print(telecom.info())  # mostra de forma resumida as informações da base dados e seus tipos.
print('\n')

# Transforma dado da coluna 'ToTalGasto' no qual o seu tipo está como texto, entretanto seu tipo deve ser númerico
telecom['TotalGasto'] = pd.to_numeric(telecom['TotalGasto'], errors='coerce')
print(telecom.info())
print('\n')

# Remove a coluna que está 100% vazia. No caso a Coluna 'Código'
telecom = telecom.dropna(how='all', axis=1)
print(telecom.info())
print('\n')

# Remove a linha que tem um item vazio
telecom = telecom.dropna()

# Analisando os Dados
# Quantos cancelaram e quantos estão ativos
print(telecom['Churn'].value_counts())
print('\n')
print(telecom['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

for column in telecom:
    if column != 'IDCliente':
        # Cria o gráfico
        graphic = px.histogram(telecom, x=column, color='Churn')
        # Exibe o gráfico
        graphic.show()
        print(telecom.pivot_table(index='Churn', columns=column, aggfunc='count')['IDCliente'])
        print('\n')
        time.sleep(1)
print('Olá')
