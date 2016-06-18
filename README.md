# Animoto_Clone
Implemented clone of Animoto -  A Distributed System to convert Images to Video using Amazon AWS
Technologies Used : Python 2.7, Instagram API, Amazon EC2,Amazon SQS and DynamoDB

Description:
- Used Instagram API to retrieve the URL of the images which will be converted to video using Amazon AWS Services
- The image URLs queued from EC2 instance(client) to SQS.
- To attain 100% efficiency, SQS stores multiple copies of the same message.
- DynamoDB deployed between SQS and worker to avoid redundancy. Message picked from the SQS, the worker update the DB with a unique message ID. 
- Image URLS downloaded into worker instance, FFMPEG is used to convert images to video. 
