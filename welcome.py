#import libraries:
import smtplib
import face_recognition
import cv2
import numpy as np
from twilio.rest import Client
import RPi.GPIO as GPIO
from time import sleep

#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

# initialize the video and allow the camera sensor to warm up
print("[INFO] Starting video...")
video = cv2.VideoCapture(0)

#Set Twilio authentication
account_sid ="xxxx" # Put your Twilio account SID here
auth_token ="xxxx" # Put your auth token here

client = Client(account_sid, auth_token)

#Set Smtplib Authentication and set the “from, to”
smtpUser = xxxx@gmail.com'
smtpPass = 'xxxx'

toAdd = 'xxxx@gmail.com'
fromAdd = smtpUser

#Encoding face for face recognition for all the person you want to the camera recognize
pierina_image = face_recognition.load_image_file("Pierina.jpg")
pierina_face_encoding = face_recognition.face_encodings(pierina_image)[0]

ryan_image = face_recognition.load_image_file("Ryan.jpg")
ryan_face_encoding = face_recognition.face_encodings(ryan_image)[0]

bill_image = face_recognition.load_image_file("Bill.jpg")
bill_face_encoding = face_recognition.face_encodings(bill_image)[0]

guido_image = face_recognition.load_image_file("Guido.jpg")
guido_face_encoding = face_recognition.face_encodings(guido_image)[0]

john_image = face_recognition.load_image_file("John.jpg")
john_face_encoding = face_recognition.face_encodings(john_image)[0]

#Store objects in array
known_face_encodings = [
    pierina_face_encoding,
    ryan_face_encoding,
    bill_face_encoding,
    guido_face_encoding,
    john_face_encoding
    ]
known_face_names = [
    "Pierina",
    "Ryan",
    "Bill",
    "Guido",
    "John"
    ]

known_face_numbers = [
    "+32xxxx",
    "+32xxxx",
    "+32xxxx",
    "+32xxxx",
    "+32xxxx"
    ]
# Your Twilio number here
sender = "+xxxx"

#Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

#Loop for the hole 
while True:
    #Grab the frame from the threaded video stream and resize it
    ret, frame = video.read()
    
    small_frame=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    #Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, :: -1]
    #Create condition

    if process_this_frame:
        
        # compute the facial embeddings for each face bounding frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        
        # loop over the facial embeddings
        for face_encoding in face_encodings:
            #See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            #Check to see if we have found a match
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
            face_names.append(name)

            #Check if there is light or not, and depending on that send text messages
            if(GPIO.input(17) == 0):
                print ("dark")
                message = client.api.account.messages.create(
                to=known_face_numbers[best_match_index], # Put your cellphone number here
                from_= sender, # Put your Twilio number here
                body="Welcome Home! " + known_face_names[best_match_index] + " Please turn ON the lights")
            else:
                print ("light")
                message = client.api.account.messages.create(
                to=known_face_numbers[best_match_index], # Put your cellphone number here
                from_= sender, # Put your Twilio number here
                body="Welcome Home! " + known_face_names[best_match_index] + " Please turn OFF the lights")
                
                        
            #Create Welcome home email alert
            header = 'To: ' + toAdd + '\n' + 'From:' + fromAdd + '\n'
            body = 'Hey ' + known_face_names[best_match_index] + ' is home'
            
            #Send Welcome Home! Email
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(smtpUser, smtpPass)
            print("Email send!")
            s.sendmail(fromAdd,toAdd,header + '\n\n'+body)

            s.quit()
            
    process_this_frame = not process_this_frame
    
    #Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        #Scale back up face locations 
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        #Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,225), 2)
        
        #Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 225), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom -6), font, 1.0, (255, 255, 255), 1)
    
    # display the image to our screen
    cv2.imshow('Video', frame)
    
    # quit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
video.release()
cv2.destroyAllWindows()
GPIO.cleanup()
