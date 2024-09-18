class auth:
    print ("auth")
    class account id:
 accountnumber:int
accountname:str
    # Simple user authentication script

# Sample user database (In practice, use a real database)
users_db = {
    "john_doe": "password123",
    "jane_smith": "my_secure_password"
}

def authenticate(username, password):
    # Check if the username exists in the database and if the password matches
    if username in users_db and users_db[username] == password:
        return "Authentication successful!"
    else:
        return "Authentication failed! Incorrect username or password."

# Example usage
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

auth_result = authenticate(username_input, password_input)
print(auth_result)