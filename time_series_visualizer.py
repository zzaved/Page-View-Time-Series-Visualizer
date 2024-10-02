import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Registra os conversores de data do Matplotlib
register_matplotlib_converters()

# Importa os dados do arquivo CSV e define a coluna 'date' como índice
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Limpa os dados removendo os valores atípicos
def clean_data(data):
    # Filtra os dados removendo os 2,5% superiores e inferiores
    lower_bound = data['value'].quantile(0.025)
    upper_bound = data['value'].quantile(0.975)
    return data[(data['value'] >= lower_bound) & (data['value'] <= upper_bound)]

# Aplica a limpeza nos dados
df = clean_data(df)

def draw_line_plot():
    # Cria um gráfico de linha para os dados de visualização de páginas
    fig, ax = plt.subplots(figsize=(12, 6))  # Define o tamanho da figura
    ax.plot(df.index, df['value'], color='blue', linewidth=1)  # Plota os dados
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')  # Título do gráfico
    ax.set_xlabel('Date')  # Rótulo do eixo x
    ax.set_ylabel('Page Views')  # Rótulo do eixo y
    
    # Salva a imagem e retorna a figura
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copia os dados e modifica para o gráfico de barras mensal
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year  # Adiciona coluna de ano
    df_bar['month'] = df_bar.index.month_name()  # Adiciona coluna de mês
    df_bar_grouped = df_bar.groupby(['year', 'month']).mean().unstack()  # Agrupa por ano e mês, calcula a média
    
    # Cria o gráfico de barras
    fig = df_bar_grouped.plot(kind='bar', figsize=(12, 6), legend=True).figure
    plt.title('Average Daily Page Views per Month')  # Título do gráfico
    plt.xlabel('Years')  # Rótulo do eixo x
    plt.ylabel('Average Page Views')  # Rótulo do eixo y
    plt.legend(title='Months')  # Título da legenda
    
    # Salva a imagem e retorna a figura
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepara os dados para os box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)  # Reseta o índice
    df_box['year'] = df_box['date'].dt.year  # Adiciona coluna de ano
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Adiciona coluna de mês
    
    # Cria os box plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))  # Define o layout com 2 gráficos
    
    # Box plot para ano
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')  # Título do gráfico
    ax1.set_xlabel('Year')  # Rótulo do eixo x
    ax1.set_ylabel('Page Views')  # Rótulo do eixo y
    
    # Box plot para mês
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')  # Título do gráfico
    ax2.set_xlabel('Month')  # Rótulo do eixo x
    ax2.set_ylabel('Page Views')  # Rótulo do eixo y
    
    # Salva a imagem e retorna a figura
    fig.savefig('box_plot.png')
    return fig