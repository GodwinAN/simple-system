# MICROSERVICE THAT RETURNS A JSON PAYLOAD OF WHETHER AN INTEGER IS ODD OR EVEN

1) Objectives
i) Create a Microservice that returns a JSON payload and performs a Data Engineering related task
ii) Push tested source code to Github and perform Continuous Integration with Github Actions (or similar SaaS Build service)
iii) Configure Build Server to Deploy Changes on build (Continuous Delivery)
iv) Create realistic API (reference here: Data Engineering: Chapter 5 aws chapter for pragmatic ai.)


2) Process

i) Continuous integration (CI) and continuous deployment (CD)

In order to ensure continuous integration and delpoyment, we used git hub actions to automatically run all the service actions and trigger a continuous integration of the service whenever the code changes and facilitate delivery for deployment whenever the cloud based service is triggered. A fast API was also built to facilitate CI/CD. 

ii) Two cloud platforms were used to deploy the microservice;
Instruction: please add the extension "/oddoreven/integer", where integer = any counting numbers greater than or eqaul to zero

AWS App runner [link](https://2awu4srmey.us-east-2.awsapprunner.com/)

AWS EC2 integrated to cloud 9 [link](http://3.140.253.214:8080/)


