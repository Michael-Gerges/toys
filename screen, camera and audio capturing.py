import keyboard, cv2, pyautogui, datetime
import numpy as np

#keyboard.write("Python Programming is always fun!", delay=0.1)
#keyboard.send("windows+d")
#while True:
#    keyboard.on_release(lambda e: print(e.name))


# static:
#fourcc = cv2.VideoWriter_fourcc(*"MJPG")
#writer = cv2.VideoWriter(r"desktop\static.avi",fourcc, 30,(640,480))
#writer.write(np.random.randint(0, 255, (480,640,3)).astype('uint8'))
#writer.release()



####on screen:

#cap = cv2.VideoCapture(0)
#print("starting")
#while True:
#    _, img = cap.read()
#    cv2.imshow("img", img)
#cap.release()
#cv2.destroyAllWindows()




### screen recording:

#SCREEN_SIZE = pyautogui.size()[0], pyautogui.size()[1]
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
#out = cv2.VideoWriter(r"desktop\output_screen1901080.avi", fourcc, 20.0, (SCREEN_SIZE))
#starting = (datetime.datetime.now().second)
#while True: # or for i in range(200):
#    img = pyautogui.screenshot()
#    frame = np.array(img)
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#    out.write(frame)
#    ending = (datetime.datetime.now().second)
#    if ending - starting > 9:  ### get 10 seconds 
#       break
#    #if cv2.waitKey(1) == ord("q"):
#    #    break



#### camera capture writer:


#cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter('capture_size_function_camera.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
#while(cap.isOpened()):
#       ret, frame = cap.read()
#       out.write(frame)
#       if cv2.waitKey(1) == ord("q"):
#           break


#cap.release()
#out.release()
#cv2.destroyAllWindows()


import pyaudio
import wave
filename = r"desktop\recording.wav"
record_seconds = 5
chunk = 1024
FORMAT = pyaudio.paInt16
channels = 1
sample_rate = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)

frames = []
print("Recording...")
for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk)
    # if you want to hear your voice while recording
    # stream.write(data)
    frames.append(data)
print("Finished recording.")
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(sample_rate)
wf.writeframes(b"".join(frames))
wf.close()