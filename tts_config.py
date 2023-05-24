from TTS.api import TTS
from TTS.tts.configs.vits_config import *
import json

# TTS Models are stores in
# /Users/bhaskarank/Library/Application Support/tts/


models = TTS().list_models()
#speakers = TTS().list_speakers()
#lang = TTS().list_languages()
print(models)
'''
c=0
while c<len(models):
    print(models[c])
    print(f"speakers for model {c+1} : ")
    speakers = TTS(models[c]).speakers
    print(speakers)
    print(f"languages for model {c+1} : ")
    languages = TTS(models[c]).languages
    print(languages)
    c+=1
    
 # store speakers list with corresponding language in a dictionary named after each model
main_dict = {}
for i in range(len(models)):
    main_dict[models[i]] = {}
    main_dict[models[i]]["speakers"] = TTS(models[i]).speakers
    main_dict[models[i]]["languages"] = TTS(models[i]).languages



# convert main_dict to json file

with open('tts_config.json', 'w') as fp:
    json.dump(main_dict, fp, indent=8)


'''