db.createUser({
    user: "myuser",
    pwd: "mypassword",
    roles: [{
        role: "readWrite",
        db: "application"
    }]
});

db.createCollection("users");
db.users.insertOne({ name: "Rajesh", age: 30 });