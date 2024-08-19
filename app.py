from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuring the email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'singh.himanshu.foruppo@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'ymwd vmza gkql ogeq'   # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'singh.himanshu.foruppo@gmail.com'  # Replace with your email

mail = Mail(app)

@app.route('/')
def index():
    return "Chatbot is running!"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data.get('message')
    step = data.get('step')
    session = data.get('session', {})

    # Logic to handle conversation steps
    if step == 1:
        response = "Hi! Welcome to our marketing agency. How can I help you today? Please choose an option:\n1. Services\n2. Pricing\n3. Portfolio\n4. Free Consultation"
        step = 2
    elif step == 2:
        if '1' in user_message:
            response = "We offer a range of services including SEO, Social Media Marketing, and Content Creation. Would you like to know more?"
        elif '2' in user_message:
            response = "Our pricing is flexible depending on the service. Would you like a detailed quote?"
        elif '3' in user_message:
            response = "You can view our portfolio on our website. Would you like the link?"
        elif '4' in user_message:
            response = "Please provide your name and email for a free consultation."
            step = 3
        else:
            response = "I didn't understand that. Please choose an option:\n1. Services\n2. Pricing\n3. Portfolio\n4. Free Consultation"
    elif step == 3:
        session['user_info'] = user_message
        response = "Thank you! We will reach out to you shortly."
        
        # Send email to the business with user details
        msg = Message("New Free Consultation Request", recipients=["xyz@gmail.com"])
        msg.body = f"User Info: {session['user_info']}"
        mail.send(msg)

        step = 1
    else:
        response = "How can I assist you?"

    return jsonify({"message": response, "step": step, "session": session})

if __name__ == '__main__':
    app.run(debug=True)
