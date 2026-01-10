from transformers import pipeline

# pipeline do transkrypcji audio (Whisper)
pipe = pipeline(
   task="automatic-speech-recognition",
   model="openai/whisper-small",   # możesz zmienić na medium/large
)

def transcribe(audio_file):
   if audio_file is None:
       return "Brak pliku audio"
   result = pipe(audio_file)
   return result["text"]


# Interfejs Gradio
demo = gr.Interface(
   fn=transcribe,
   inputs=gr.Audio(type="filepath", label="Wgraj plik audio (MP3/WAV)"),
   outputs=gr.Textbox(label="Transkrypcja"),
   title="Whisper ASR w Dockerze",
   description="Prześlij plik audio, a model Hugging Face (Whisper) dokona transkrypcji."
)
