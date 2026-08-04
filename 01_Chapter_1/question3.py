import os

os.system('powershell -c "Add-Type –AssemblyName System.Speech; \
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; \
$speak.Speak(\'Hello Mamta how are you\');"')
