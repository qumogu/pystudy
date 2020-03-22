users =[
    {
        "name":"jack",
        "age":18,
        "phone":"12345"
    },
    {
        "name":"may",
        "age":22,
        "phone":"12345"
    }
]

for user in users:
    user["age"]  += 1 
    user["school"]  = "UC School"
    user.pop("phone")

print(users)