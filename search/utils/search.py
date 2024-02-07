import openai

from decouple import config

from ..models import Documents

from ..serializer import Documentserializer

openai.api_key = config('OPENAI_KEY') 

def semantic_search(query, documents, searchType):
    
    prompt = ' '
    if searchType == 'Single' : 
        prompt = f"{documents}\nSemantic search return first matching document name {query} return response  in dictionary format"
        
    else :
        prompt = f"{documents}\nSemantic search return documents name   where score >= 0.5 {query} return response in dictionary format"

    # Call the OpenAI API
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # You may need to update the model name
        prompt=prompt,
        temperature=0,
        max_tokens=200,
        n=1,
        stop=None
    )

    # Extract and return the selected document
    selected_document = response['choices'][0]['text']
    return selected_document



def retrive_documents():
        queryset = Documents.objects.all()
        serilaizedData = Documentserializer(queryset,many=True)
        return (serilaizedData.data)
