import requests

url = 'http://localhost/testimg/save_image.php'
files = {'image': open('/home/pi/uploadimg/image1.jpg', 'rb')}
try:
        response = requests.post(url, files=files,timeout=60)
        print response
except requests.exceptions.RequestException as e:
        print "Error: {}".format(e)
        print "time out error"
