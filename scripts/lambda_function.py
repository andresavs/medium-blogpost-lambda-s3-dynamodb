import json
import urllib.parse
from pprint import pprint
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb')

    # Recuperar o nome do bucket do payload 
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # Recuperar nome do arquivo do payload 
    nomearquivo = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        
        # Buscar o arquivo do bucket S3
        arquivo = s3.get_object(Bucket=bucket, Key=nomearquivo)
        
        # Desserializar o conteúdo do arquivo
        texto = arquivo['Body'].read().decode()
        dados = json.loads(texto)
        
        # Print do conteúdo do arquivo
        # print(dados)
        
        # Iteração para selecionar as colunas e gravar os dados no DynamoDB 
        for registros in dados:
            
            #Print dos itens selecionados
            #print(registros['Região'],registros['Sigla'],registros['Estado'],registros['População'])
            
            tabela = dynamodb.Table('populacao-pib-estados-brasil')
            tabela.put_item(Item={
                'regiao': registros['Região'],
                'uf': registros['Sigla'],
                'nome': registros['Estado'],
                'populacao': str(registros['População']),
                'pib': str(registros['PIB (R$)'])
            })

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(nomearquivo, bucket))
        raise e