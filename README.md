# Language-Prediction
Explore language prediction effortlessly with our Python, Flask, and Docker combo. Deploy, share on Docker Hub, and access the API seamlessly via Postman. Streamlined natural language processing at your fingertips! 🌐💬 #Python #Flask #Docker #NLP

# Files Arrangement 
1. Create a directory/folder that will contain the projet (ex.; named as 'Language Prediction Project')
2. In this directory, set the following files (app2, Dockerfile, model, requirements, and trained_pipeline-0.1.0.pkl).
3. Then create 2 directory inside 'Language Prediction Project' file
4. first directory named 'templates', in which the html file will placed (index.html)
5. the second named 'modelAndDataset', where the dataset and the python code (your model) will be in it (Language Detection.csv, Language Detection.ipynb)

# Steps to upload the project on docker
1. open the command prompt on the main directory of the project ('Language Prediction Project' file)
2. write the following comman: docker build -t (the name of the docker image from your choise)
3. press ENTER

# How to interact with our language prediction API?
1. open Postman, a powerful tool for testing and exploring APIs.
2. Identify Docker Container IP
3. Create a New Request: Click on the "New" button in Postman to create a new request.
4. Configure Request: In the request tab, specify the following: 1) Request Type: Choose the appropriate HTTP method (e.g., POST). 2) URL: Enter the URL of your Flask API endpoint. It should be in the format http://<container_ip>:<port>/your_endpoint. 3) Headers: Add any necessary headers (e.g., Content-Type).
5. Add Request Body: If your Flask API expects input data, switch to the "Body" tab in Postman. Enter the necessary input data in the desired format (JSON), (ex.; { "text_input": "مرحبا" }).
6. Send Request: Click the "Send" button to send the request to your Flask API. 
7. View Response: Postman will display the response from the Flask API. This should include the language prediction based on the input provided.
8. Repeat for Additional Requests: You can repeat the process for different inputs to observe real-time language predictions.
By following these steps, you can use Postman to interact with your Flask API running in a Docker container. This allows you to send requests, receive language predictions in real-time, and test the functionality of your language prediction project effortlessly.
