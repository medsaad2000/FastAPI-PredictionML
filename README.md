# UEFA CL Predictions

<h2>Deploye a ML model (Football Match Probability Prediction) as an API using FastAPI</h2>

<p> Integrating a ML predective model to a web application using Fast API in the Backend and Angular 13 in the Frontend </p>

<h3>For more details about this project: </h3>
<p>Here's the links of the Frontend Repository & the notebook of our model </p>
<p><strong>->The ML Model  :</strong> https://github.com/medsaad2000/Football-Match-Probability-Prediction</p>
<p><strong>->Frontend Repository (Angular 13) :</strong> https://github.com/medsaad2000/Front-PredictionML </p>
<h3>Backend :</h3>
<p>Technologie used : Python, FastAPI as a framework </p>

![fasta](https://user-images.githubusercontent.com/81382178/169704216-444fdf72-be98-4b31-b94f-bcd16fbd8338.png)

<h3>To Run the project :</h3>
1 - Install FastApi and Uvicorn : `pip3 install uvicorn fastapi` 
<br/>
2 - Run the project : `uvicorn app:app --reload`

<h3>Testing our API: </h3>
<p>To test our API we’ll be using Swagger UI now to access that you’ll just need to add /docs at the end of your path. So go to http://127.0.0.1:8000/docs. And you should see the following output:</p>

![Screenshot 2022-05-22 165606](https://user-images.githubusercontent.com/81382178/169704415-4074e342-cdce-4a8d-b4ef-5a0e16ab987b.png)

<p>After you’ve entered all the values (Home Team Name & Away Team Name) click on Execute, after this you can see your output under the responses section</p>

![Screenshot 2022-05-22 165843](https://user-images.githubusercontent.com/81382178/169704485-8ee5a87a-44f8-4a9f-a914-792160b11c30.png)

<h3>GUI : (Angular 13)</h3>

<p>First Page</p>

![App](https://user-images.githubusercontent.com/81382178/169704898-896fa7f3-4a73-4588-ba83-f12884053176.png)

<p>We select the Home Team Name & Away Team Name</p>


![App 2](https://user-images.githubusercontent.com/81382178/169704926-6bb40d17-2b1d-4925-9f81-1bf31dea47f1.png)

<p>For example : We choose here Paris Saint Germain VS Juventus and then we click <strong>predict</strong></p>

![App 3](https://user-images.githubusercontent.com/81382178/169704956-83e206a1-e4ef-4761-93db-dcca193a6c35.png)

<p>Results :</p>

![App 4](https://user-images.githubusercontent.com/81382178/169704975-d0b8701c-4065-499f-91dd-1f455365e238.png)





