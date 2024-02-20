import pandas as pd
import os
import warnings

# Desativar temporariamente os avisos relacionados ao openpyxl
warnings.simplefilter("ignore", UserWarning)

def converte_para_csv(diretorio_origem, diretorio_destino):
    # Listar todos os arquivos .xlsx no diretório de origem
    arquivos_xlsx = [arquivo for arquivo in os.listdir(diretorio_origem) if arquivo.endswith('.xlsx')]

    # Converter cada arquivo .xlsx para .csv
    for arquivo in arquivos_xlsx:
        # Ler o arquivo .xlsx
        df = pd.read_excel(os.path.join(diretorio_origem, arquivo), engine='openpyxl')

        # Definir o caminho e nome do arquivo .csv
        caminho_csv = os.path.join(diretorio_destino, f"{arquivo.split('.')[0]}.csv")

        # Salvar o arquivo .csv separado por tabulação
        df.to_csv(caminho_csv, sep='\t', index=False)

# Diretório onde estão os arquivos .xlsx
diretorio_origem = 'C:/Users/vinicius.pereira/Documents/GitHub/converter-xlsx-to-csv/excel/'

# Diretório onde serão salvos os arquivos .csv
diretorio_destino = 'C:/Users/vinicius.pereira/Documents/GitHub/converter-xlsx-to-csv/csv/'

# Converter arquivos .xlsx para .csv separados por tabulação
converte_para_csv(diretorio_origem, diretorio_destino)
