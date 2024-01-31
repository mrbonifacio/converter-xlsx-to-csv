import pandas as pd
import os
import warnings

# Desativar temporariamente os avisos relacionados ao openpyxl
warnings.simplefilter("ignore", UserWarning)

def converte_para_csv():
    # Definir o diretório onde estão os arquivos .xlsx
    diretorio = f'C:/Users/{os.getlogin()}/temp/excel/'
    destino = 'C:\\Users\\vinicius.pereira\\Documents\\GitHub\\unificador-csv\\baseCarteira\\'

    # Listar todos os arquivos .xlsx no diretório
    arquivos_xlsx = [arquivo for arquivo in os.listdir(
        diretorio) if arquivo.endswith('.xlsx') and 'HISTORICO_AGENDAMENTO' in arquivo]

    # Converter cada arquivo .xlsx para .csv separado por tabulação
    for arquivo in arquivos_xlsx:
        # Ler o arquivo .xlsx
        df = pd.read_excel(os.path.join(diretorio, arquivo), engine='openpyxl')

        # Definir o caminho e nome do arquivo .csv
        caminho_csv = os.path.join(destino, f"{arquivo.split('.')[0]}.csv")

        # Salvar o arquivo .csv separado por tabulação
        df.to_csv(caminho_csv, sep='\t', encoding='utf-16', index=False)

converte_para_csv()
