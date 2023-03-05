# Disease-model
Tumour disease with flask


This is a Python Flask web application that models the immune response to cancer using ODEs and displays the results on a webpage. Here is a brief explanation of the code:

Import the necessary libraries: Flask for building the web app, numpy and matplotlib for scientific computing and data visualization, and odeint from scipy.integrate for solving the ODEs.

Define the model() function that takes in five variables y, t, rC, dC, rH, kIL, kCT, s, K and returns a list of the derivatives of the five state variables C, H, IL, T, S. This function represents the ODEs that describe the interactions between cancer cells, immune cells, and the immune response.

Define the route for the homepage using the @app.route() decorator. If the form has been submitted, the model parameters are updated based on the user input. Then, the odeint() function is used to solve the ODEs using the updated parameters. The results are plotted using matplotlib and saved as a PNG file in the static directory. Finally, the homepage template index.html is rendered with the current parameter values and the graph.

Define the route for the results page using the @app.route() decorator. The results template results.html is rendered, which displays the saved graph from the previous step.

Run the app using app.run() and set the debug flag to True for debugging.

Note that the web app consists of two templates (index.html and results.html) located in the templates directory and a static file (plot.png) located in the static directory.


![image](https://user-images.githubusercontent.com/57437701/222965327-303e9980-34de-45a6-b250-a80a85edc428.png)
