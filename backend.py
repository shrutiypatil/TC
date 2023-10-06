from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Your MySQL database configuration

@app.route('/')
def index():
    return render_template('service.html')  # Serve the frontend HTML file

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.form
    name = data['name']
    email = data['email']
    message = data['message']

    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert feedback data into the database
        cursor.execute("INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Feedback submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
