import requests

# r = requests.post("http://localhost:5000/exchange", json={'data': 137})
r = requests.post("https://ravevirtualpet.herokuapp.com/exchange", json={'data': 137})

if r.status_code == requests.codes.ok:
    data = r.json()
    print("Data OK: ", data)
else:
print("error fetching, status is ", r.status_code)
