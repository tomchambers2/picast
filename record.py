import boto

#bind to clicker and check state on/off, if on run record()

#record() - launches arecord and returns with wav


#upload() - upload file to server

s3 = boto.connect_s3()
bucket = s3.create_bucket('media.picast')
key = bucket.new_key('')