from flask import Flask, request, jsonify
import jinja2

with open('style.css', 'r') as f:
    css_content = f.read()


app = Flask(__name__)

@app.route('/')

def home():
    return f"""
    <html>
        <style>
        {css_content}
        </style>

        <body>
            <h1>Welcome to NotRapnik!</h1>
            <p>This is a simple Flask application.</p>
            <div class="mycontainer">   
                <div style="background-color:#CBF123;">
                <h2>Jakis tekst</h2>
                </div>

                
                <div style="background-color:#FCF4B3;">
                <h2>NotRapnik</h2>
                </div>

                
                <div style="background-color:#FFF4A3;">
                  <h2>Podaj login:</h2>
                  <input type="text" id="login_email">
                  <h2>Podaj hasło:</h2>
                  <input type="password" id="login_password">
                  <br><br>
                    <button type="button" onclick="login()">Zaloguj</button>
                    <button type="button" onclick="register()">Zarejestruj</button>
                </div>
            </div>



            <!-- Firebase App (the core Firebase SDK) -->
            <script src="https://www.gstatic.com/firebasejs/11.10.0/firebase-app.js"></script>
            <!-- Firebase Analytics -->
            <script src="https://www.gstatic.com/firebasejs/11.10.0/firebase-analytics.js"></script>
            <!-- Firebase Auth (required for authentication) -->
            <script src="https://www.gstatic.com/firebasejs/11.10.0/firebase-auth.js"></script>
            <script>
var firebaseConfig = {{
    apiKey: "AIzaSyDqlxg9mj9OQRfFOaRum1FMKqT9DhLrJWo",
    authDomain: "notrapnik.firebaseapp.com",
    projectId: "notrapnik",
    storageBucket: "notrapnik.firebasestorage.app",
    messagingSenderId: "140767632135",
    appId: "1:140767632135:web:369e340da56721cb3643a2",
    measurementId: "G-Q9SY3RP2GG"
}};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

// Login function
function login() {{
    console.log("Login function called");
    var email = document.getElementById('login_email').value;
    var password = document.getElementById('login_password').value;
    firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {{
        alert('Logged in as: ' + userCredential.user.email);
    }})
    .catch((error) => {{
        alert(error.message);
    }});
}}

// Register function
function register() {{
    var email = document.getElementById('login_email').value;
    var password = document.getElementById('login_password').value;
    firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {{
        alert('Registered as: ' + userCredential.user.email);
    }})
    .catch((error) => {{
        alert(error.message);
    }});
}}
</script>
        </body>
    </html>
    """

@app.route('/api/data', methods=['GET'])

def get_data():
    data = {
        "message": "This is some sample data",
        "status": "success"
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])

def post_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"received": data, "status": "success"}), 201


if __name__ == '__main__':
    app.run(debug=True)
