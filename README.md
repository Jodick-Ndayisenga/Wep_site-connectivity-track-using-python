##Webpage Checker - Monitoring Websites for Accessibility and Errors

Introduction:
The code provided is a Python program that monitors the accessibility of a webpage or website by opening the link once every 60 seconds. It uses the urllib library to handle URL-related operations, such as opening URLs and catching errors. The program checks for HTTP errors and URL opening errors and provides feedback to the user accordingly.

Main Features:

    URL Monitoring: The program uses a while loop to repeatedly check the accessibility of the provided URL using urllib.request.urlopen() method.
    Error Handling: The program catches HTTP errors and URL opening errors using try-except blocks. If an error occurs, it displays a corresponding error message with the error code and the URL that was checked.
    Success Notification: If no errors occur, the program displays a success message indicating that the website is accessible and up-to-date.
    Time Delay: The program uses time.sleep() method to pause execution for 60 seconds after each URL check, allowing for periodic monitoring of the website.

Documentary:
[Visuals: Show the code being executed in a Python environment, with comments and explanations appearing as the code is being executed]

Narrator: "Welcome to the Webpage Checker documentary. In this program, we will be exploring how Python can be used to monitor the accessibility of a webpage or website. Let's take a closer look at the code."

[Visuals: Zoom in on the code with comments, highlighting relevant sections]

Narrator: "The code starts by importing the necessary libraries - time, urllib.error, and urllib.request - to handle URL-related operations and manage time delays."

[Visuals: Show the import statements in the code]

Narrator: "The main function, check_url(), takes a parameter called my_website, which is the URL of the webpage or website to be monitored. It uses a while loop to repeatedly check the accessibility of the URL."

[Visuals: Show the while loop in the code]

Narrator: "Inside the while loop, the program uses the urllib.request.urlopen() method to open the URL and establish a connection. If an HTTP error occurs, it is caught using the except block for urllib.error.HTTPError and a corresponding error message is displayed with the error code and the URL that was checked."

[Visuals: Show the try-except block for HTTP errors in the code, with an example error message being displayed]

Narrator: "Similarly, if a URL opening error occurs, it is caught using the except block for urllib.error.URLError and a corresponding error message is displayed with the error code and the URL that was checked."

[Visuals: Show the try-except block for URL opening errors in the code, with an example error message being displayed]

Narrator: "If no errors occur, the program displays a success message indicating that the website is accessible and up-to-date."

[Visuals: Show the success message being displayed in the code]

Narrator: "After each URL check, the program pauses execution for 60 seconds using the time.sleep() method, allowing for periodic monitoring of the website."

[Visuals: Show the time.sleep() method being used in the code]

Narrator: "Finally, the code includes a condition to check if the script is being executed as the main program, and if so, it calls the check_url() function with a sample URL to start the monitoring process."

[Visuals: Show the if name == 'main': condition and the check_url() function being called with a sample URL in the code]

Narrator: "And that's it! With this code, you can easily monitor the accessibility of a webpage or website by opening the link once every 60 seconds, catch HTTP errors and URL opening errors, and receive notifications
