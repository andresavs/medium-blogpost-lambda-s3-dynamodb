# medium-blogpost-lambda-s3-dynamodb
Exemplos utilizados para um Hands-On e que gerou alguns blogposts no Medium - Função Lambda em Python, que será executada automaticamente quando o um upload de um arquivo .json for realizado no Bucket S3, ela fará a leitura dos dados e criará registros em uma tabela do DynamoDB. E como um plus todos os recursos que criamos pelo console da AWS também será possível criar via template de CloudFormation!

Links do Medium:
Artigo Hands-On: [Importando dados do S3 para o DynamoDB usando uma Lambda Function](https://andresaviana.medium.com/importando-dados-do-s3-para-o-dynamodb-usando-uma-lambda-function-33768c387956)

Artigo de Introdução para AWS Lambda: [AWS Lambda x Lambda Function x Lambda Application x Lambda@Edge](https://andresaviana.medium.com/aws-lambda-x-lambda-function-x-lambda-application-x-lambda-edge-15015be1812e)


Artigo introdutório sobre CloudFormation + Stack que utilizamos no Artigo Hands-On: [Entendendo AWS CloudFormation](https://andresaviana.medium.com/entendendo-aws-cloudformation-f292b9a2e6cb)


### Estrutura

- ./dados/CustomPolicy_LambdaS3DynamoDB.json - .json da Policy customizada que criamos no IAM.
- ./dados/dados-estados-brasil.json - Arquivo com os dados de PIB e População dos estados brasileiros. Fonte: (IBGE 2010)
- ./dados/lambda-test-event.json - Paylod S3 extraído do [site AWS](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html). Utilizado para testar a função lambda pelo console, simula o upload de arquivo no bucket S3.
    - Necessário alterar linha 23 (nome do seu bucket S3) e linha 30 (nome do arquivo que está no bucket S3).


- ./scripts/lambda_function.py - Script básico em python que faz leitura do arquivo no bucket S3 e cria os registros no DynamoDB.

- ./stack-CloudFormation/template.yml - Template de CloudFormation que cria a mesma stack que criamos via console no Artigo Hands-On.
- ./stack-CloudFormation/ttemplate-changeset.yml - Cópia do template.yml com um bucket a mais para criar um change stack.


### Observações

- Script Python tem alguns prints comentados, eles foram usados para teste com jupyter notebook na construção do código. E usados como exemplo do Hands-On, mas **não devemos colocar print em Lambda Function**.

- O template de CloudFormation não está seguindo as melhores práticas em algumas seções como Metadatas e Parameters, por exemplo, pois queria demonstrar algumas opções nesse Hands-On. Mais detalhes no artigo do medium.
