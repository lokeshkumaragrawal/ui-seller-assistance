from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'your key'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    print(message)
    try:
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[
            {"role": "system", "content": "You are a helpful assistant of a ui kit selling company. You are helping a user to find the best ui kit for his project. The user is asking for a ui kit for a project that is related to a social media app. He wants to know about the best ui kit for his project. you have to help him to find the best ui kit for his project by any false value"},
            {"role": "user", "content": message}
        ])
        response = completion.choices[0].message
    except Exception as e:
        print(e)
        response = 'Failed to Generate response!'
    # Return the response as a JSON object
    print(response)
    return {"message": response}
    

if __name__=='__main__':
    app.run()

