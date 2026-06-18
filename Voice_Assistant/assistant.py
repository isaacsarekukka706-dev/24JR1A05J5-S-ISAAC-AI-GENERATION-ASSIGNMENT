from gtts import gTTS
import os

print("🎤 AI Voice Assistant")

question = input("Ask a question: ")

responses = {
    "what is artificial intelligence":
        "Artificial Intelligence is the simulation of human intelligence by machines.",
    
    "what is machine learning":
        "Machine Learning is a branch of AI that allows computers to learn from data.",

    "what is python":
        "Python is a popular programming language used for web development, data science, and AI."
}

answer = responses.get(
    question.lower(),
    "Sorry, I do not know the answer."
)

print("Assistant:", answer)

tts = gTTS(text=answer, lang="en")

tts.save("response.mp3")

print("Audio response saved as response.mp3")
