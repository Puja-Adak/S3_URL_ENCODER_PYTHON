# importing sys
import sys
 # adding Folder_2 to the system path
sys.path.insert(0, 'C:\Github\S3_URL_ENCODER_PYTHON\SOurce')

from S3Encoder import s3Encode

#S3 bucket structure {my_bucket_name}\folder name \filename

# key is "folder name \filename" to download the S3 file 

 
#test case 1

S3_keyname = "input\Z00010246+%281%29.PNG"
print(s3Encode(S3_keyname))
# output 
#input\Z00010246%2B%281%29.PNG


#test case 2

S3_keyname = "input\Z00010246 %281%29.PNG"
print(s3Encode(S3_keyname))
#output = input\Z00010246%2B%281%29.PNG

#test case 3

S3_keyname = "input\Z00010246.png"
print(s3Encode(S3_keyname))
#output = input\Z00010246.png


#test case 4

S3_keyname = "input\Z00010246 %28-1%29.png"
print(s3Encode(S3_keyname))
#output = input\Z00010246%2B%28%E2%801%29.png
