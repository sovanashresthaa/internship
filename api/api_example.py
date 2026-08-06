# ##API CALL 
# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# print(response)



#read JSON data 

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# data = response.json()

# print(data)


#Print only names 

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# users = response.json()

# for user in users:
#     print(user["name"])


#Print only names and emails

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# users = response.json()

# for user in users:
#     print("Name :", user["name"])
#     print("Email:", user["email"])
#     print()


#Print company names

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# users = response.json()

# for user in users:
#     print(user["company"]["name"])


#check if the req succeded

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# if response.status_code == 200:
#     print("API request successful")
# else:
#     print("API request failed")