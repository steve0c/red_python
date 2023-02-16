import boto3


import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='Functions are hard!' ,
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )

    print(response)  

translate_text() 
