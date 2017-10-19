import picamera
from time import sleep

camera = picamera.PiCamera()

camera.capture('image1.jpg')
print 'Capture Image1'
sleep(5)
camera.capture('image2.jpg')
print 'Capture Image2'

