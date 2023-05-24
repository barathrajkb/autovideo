from TTS.api import TTS
from TTS.tts.configs.vits_config import *

# Running a multi-speaker and multi-lingual model
models = TTS().list_models()
model =['tts_models/multilingual/multi-dataset/your_tts', 'tts_models/bg/cv/vits', 'tts_models/cs/cv/vits',
        'tts_models/da/cv/vits', 'tts_models/et/cv/vits', 'tts_models/ga/cv/vits', 'tts_models/en/ek1/tacotron2',
        'tts_models/en/ljspeech/tacotron2-DDC', 'tts_models/en/ljspeech/tacotron2-DDC_ph','tts_models/en/ljspeech/glow-tts',
        'tts_models/en/ljspeech/speedy-speech','tts_models/en/ljspeech/tacotron2-DCA', 'tts_models/en/ljspeech/vits', 
        'tts_models/en/ljspeech/vits--neon', 'tts_models/en/ljspeech/fast_pitch','tts_models/en/ljspeech/overflow', 
        'tts_models/en/ljspeech/neural_hmm','tts_models/en/vctk/vits', 'tts_models/en/vctk/fast_pitch',
        'tts_models/en/sam/tacotron-DDC','tts_models/en/blizzard2013/capacitron-t2-c50', 
        'tts_models/en/blizzard2013/capacitron-t2-c150_v2','tts_models/en/multi-dataset/tortoise-v2', 
        'tts_models/en/jenny/jenny', 'tts_models/es/mai/tacotron2-DDC','tts_models/es/css10/vits', 
        'tts_models/fr/mai/tacotron2-DDC', 'tts_models/fr/css10/vits','tts_models/uk/mai/glow-tts', 'tts_models/uk/mai/vits',
        'tts_models/zh-CN/baker/tacotron2-DDC-GST', 'tts_models/nl/mai/tacotron2-DDC', 'tts_models/nl/css10/vits', 
        'tts_models/de/thorsten/tacotron2-DCA', 'tts_models/de/thorsten/vits', 'tts_models/de/thorsten/tacotron2-DDC', 
        'tts_models/de/css10/vits-neon', 'tts_models/ja/kokoro/tacotron2-DDC', 'tts_models/tr/common-voice/glow-tts', 
        'tts_models/it/mai_female/glow-tts', 'tts_models/it/mai_female/vits', 'tts_models/it/mai_male/glow-tts', 
        'tts_models/it/mai_male/vits', 'tts_models/ewe/openbible/vits', 'tts_models/hau/openbible/vits', 
        'tts_models/lin/openbible/vits', 'tts_models/tw_akuapem/openbible/vits', 'tts_models/tw_asante/openbible/vits', 
        'tts_models/yor/openbible/vits', 'tts_models/hu/css10/vits', 'tts_models/el/cv/vits', 'tts_models/fi/css10/vits', 
        'tts_models/hr/cv/vits', 'tts_models/lt/cv/vits', 'tts_models/lv/cv/vits', 'tts_models/mt/cv/vits', 
        'tts_models/pl/mai_female/vits', 'tts_models/pt/cv/vits', 'tts_models/ro/cv/vits', 'tts_models/sk/cv/vits', 
        'tts_models/sl/cv/vits', 'tts_models/sv/cv/vits', 'tts_models/ca/custom/vits', 'tts_models/fa/custom/glow-tts', 
        'tts_models/bn/custom/vits-male', 'tts_models/bn/custom/vits-female']
# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
for c in range(len(models)):
    model_name = TTS.list_models()[c]
    tts = TTS(model_name, progress_bar=False, gpu=False)
    file = f'all/file{c}.mp3'
    if tts.speakers == None and tts.languages == None:
        tts.tts_to_file(text="Hello World", file_path= file)
    elif tts.speakers == None:
        tts.tts_to_file(text="Hello World", language=tts.languages[0], file_path= file)
    elif tts.languages == None:
        tts.tts_to_file(text="Hello World",speaker=tts.speakers[0], file_path= file)
    else:
        tts.tts_to_file(text="Hello World",speaker=tts.speakers[0], language=tts.languages[0], file_path= file)


# Init TTS with the target model name
#tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)
# Run TTS

# Run TTS with emotion and speed control
# tts.tts_to_file(text="This is a test.", file_path=OUTPUT_PATH, emotion="Happy", speed=1.5)


# Example text to speech using [🐸Coqui Studio](https://coqui.ai) models. You can use all of your available speakers in the studio.
# [🐸Coqui Studio](https://coqui.ai) API token is required. You can get it from the [account page](https://coqui.ai/account).
# You should set the `COQUI_STUDIO_TOKEN` environment variable to use the API token.

