import pyaudio as pa
import wave as w
import speech_recognition as sr
import random
def speech():
	chunk=1024
	Format=pa.paInt24
	channels=2
	rate=48000
	p=pa.PyAudio()
	duration=5
	o=input("what do you want to name the output file ?")
	outname=f"{o}.wav"
	stream = p.open(format= Format ,
					channels=channels,
					rate=rate,
					input=True,
					frames_per_buffer=chunk)
	c1=(rate*duration)//chunk
	collection=[]
	print("recording now")
	for i in range(0,c1):
		data=stream.read(chunk)
		collection.append(data)
	print("stopped recoding")
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf=w.open(outname,'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(p.get_sample_size(Format))
	wf.setframerate(rate)
	wf.writeframes(b''.join(collection))
	wf.close()
	r=sr.Recognizer()
	source=sr.AudioFile(outname)
	with source as source:
		audio=r.record(source)
		c=(r.recognize_google(audio,show_all=True))
	if c:
		return (r.recognize_google(audio))
	else:
		print("Oops you did not say anything")
def rockpaperscissor():
	s1=speech()
	s1=s1.lower()
	if s1:
		if "rock" in s1:
			player_1=1
		elif "paper" in s1:
			player_1 =2
		else:
			player_1=3
	return player_1
def RPS():
	rock, paper, scissors, p2 = 1, 2, 3, random.randint(1,3)
	p1 = rockpaperscissor()
	if p1 == p2:
		print ("tie")
	else:
		x=((p1-p2)%3)
		print(f"p{x} won")
RPS()