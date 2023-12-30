# Language-Prediction
Explore language prediction effortlessly with our Python, Flask, and Docker combo. Deploy and access the API seamlessly via Postman. Streamlined natural language processing at your fingertips! 🌐💬 #Python #Flask #Docker #NLP

# Files Arrangement
1. Create a directory or folder that will contain the project (ex., named 'Language Prediction Project').
2. In this directory, set the following files (app2, Dockerfile, model, requirements, and trained_pipeline-0.1.0.pkl).
3. Then create two directories inside the 'Language Prediction Project' file.
4. the first directory named 'templates', in which the HTML file will be placed (index.html).
5. the second named'modelAndDataset', where the dataset and the Python code (your model) will be in it (Language Detection.csv, Language Detection.ipynb).

# Steps to upload the project to Docker
1. Open the command prompt in the main directory of the project (the 'Language Prediction Project' file).
2. Write the following command: docker build -t (the name of the docker image from your choice)
3. Press ENTER.

# How do you interact with our language prediction API?
1. Open Postman, a powerful tool for testing and exploring APIs.
2. Identify the Docker container IP.
3. Create a New Request: Click on the "New" button in Postman to create a new request.
4. Configure Request: In the request tab, specify the following: 1) Request Type: Choose the appropriate HTTP method (e.g., POST). 2) URL: Enter the URL of your Flask API endpoint. It should be in the format http://<container_ip>:<port>/your_endpoint. 3) Headers: Add any necessary headers (e.g., Content-Type).
5. Add Request Body: If your Flask API expects input data, switch to the "Body" tab in Postman. Enter the necessary input data in the desired format (JSON) (ex., { "text_input": "مرحبا" }).
6. Send Request: Click the "Send" button to send the request to your Flask API.
7. View Response: Postman will display the response from the Flask API. This should include the language prediction based on the input provided.
8. Repeat for Additional Requests: You can repeat the process for different inputs to observe real-time language predictions.

By following these steps, you can use Postman to interact with your Flask API running in a Docker container. This allows you to send requests, receive language predictions in real-time, and test the functionality of your language prediction project effortlessly.
