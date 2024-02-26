# This is the Python/Flask File for anything ticketing related. It will hold all relevant parts of the ticketing system.

# 1. Import necessary libraries: flask, MongoClient from pymongo.

# 2. Initialize Flask app:
#     a. Create a Flask app instance.

# 3. MongoDB connection:
#     a. Create a MongoClient instance pointing to the MongoDB server.
#     b. Specify the database and collection to use.

# 4. Define a route '/submit_ticket' to handle POST requests:
#     a. Use the route decorator with the method parameter set to ['POST'].
#     b. Define a function named submit_ticket to handle the request:
#         i. Get ticket data from the HTML form using flask.request.form.
#         ii. Insert ticket data into MongoDB using collection.insert_one().
#         iii. Return a success message.

# 5. Main function to run the Flask app:
#     a. Check if the script is being run directly (__name__ == '__main__').
#     b. If it is, run the Flask app using app.run() with debug mode enabled.

# 6. Implement HTML form on the frontend to capture ticket information and send it to the '/submit_ticket' endpoint of the Flask app.

# 7. Ensure that MongoDB is running on localhost and listening on port 27017.

# 8. Test the script by submitting ticket information through the HTML form and verifying that it is stored in the MongoDB database.