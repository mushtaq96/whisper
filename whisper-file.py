import whisper

# whisper has multiple models that you can load as per size and requirements
# specify 'cuda' to use GPU
model = whisper.load_model("tiny.en")

# path to the audio file you want to transcribe
PATH = "C:\\Users\\BOKHARS\\Downloads\\17 Oct, 12.32 pm.aac"

result = model.transcribe(PATH)  
print(result["text"])
