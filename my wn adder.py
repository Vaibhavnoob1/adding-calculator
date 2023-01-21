import pyttsx3 as pyt
a = input("put number one:")
b = input("put number two:")
ans = int(a) + int(b)
print("the ans is", ans)
pyt.speak("the answer is")
pyt.speak(ans)
