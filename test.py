import S3Decoder as S3Decoder

#S3 bucket structure {my_bucket_name}\folder name \filename

# key is "folder name \filename" to download the S3 file 


#test case 1

S3_keyname = "input\Z00010246+%281%29.PNG"
print(S3Decoder.s3decode(S3_keyname))
# output 
#input\Z00010246 (1).PNG


#test case 2

S3_keyname = "input\Z00010246 %281%29.PNG"
print(S3Decoder.s3decode(S3_keyname))
#output = input\Z00010246 (1).PNG

#test case 3

S3_keyname = "input\Z00010246.png"
print(S3Decoder.s3decode(S3_keyname))
#output = input\Z00010246.png


#test case 4

S3_keyname = "input\Z00010246 %28-1%29.png"
print(S3Decoder.s3decode(S3_keyname))
#output = input\Z00010246 (-1).png
