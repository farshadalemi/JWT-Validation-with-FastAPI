import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import ContactSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer


# Test Data
MyContacts = [
    {
        "id": 1,
        "name": "Farshad",
        "phone": "09124320565",  
        "email": "farshad.alemi@gmail.com",
        "created_at": "2024-10-09T12:34:56.789123",
        "updated_at": "2024-10-09T12:54:33.229123",
        "delete_flag": 0,
        "deleted_at": ""
    },
    {
        "id": 2,
        "name": "Asghar",
        "phone": "09123456789",  
        "email": "Asghar@gmail.com",
        "created_at": "2022-10-01T12:34:56.789123",
        "updated_at": "2022-10-01T12:54:33.229123",
        "delete_flag": 0,
        "deleted_at": ""
    },
]


UsersList = []


app = FastAPI()


# Get Method | Fetch All Contacts
@app.get("/contacts", tags=["contacts"])
def get_all_contacts():
    return{"data":MyContacts}


# Get Method | Fetch Contacts by {id}
@app.get("/contacts/{id}", tags=["contacts"])
def get_contacts_by_id(id : int):
    if id > len(MyContacts):
        return{"error":"id not found"}
    for contacts in MyContacts:
        if contacts["id"] == id:  
            return{ 
                "data":contacts
            }
        

# Post method | Add Contact
@app.post("/contacts", dependencies=[Depends(jwtBearer())],tags=["contacts"])
def addContact(contact: ContactSchema):
    contact.id = len(MyContacts) + 1
    MyContacts.append(contact.dict())
    return {
        "info":"Contact Added!"
    }


# User Signup method
@app.post("/users/signup", tags=["users"])
def user_signup(user : UserSchema = Body(default = None)):
    UsersList.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in UsersList:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    

@app.post("/user/login", tags=["users"])
def user_login(user : UserLoginSchema = Body(default = None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "Invalid Login Details!"
            }