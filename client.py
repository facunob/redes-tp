import requests, json, sys

host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
apiUrl = f'http://{host}:8000/api'


# GET all
print(f'GET {apiUrl}')
resp = requests.get(apiUrl)
get_all_response = json.loads(resp.content)
print(get_all_response)


# GET by id
print(f'GET {apiUrl}/1')
resp = requests.get(f'{apiUrl}/1')
get_id = json.loads(resp.content)
print(get_id)


# DELETE by id
print(f'DELETE {apiUrl}/1')
resp = requests.delete(f'{apiUrl}/1')
delete_id = json.loads(resp.content)
print(delete_id)


# POST
print(f'POST {apiUrl}')
resp = requests.post(
      apiUrl,
      json = {
          "author": "nuevo autor"
      }
    )
print(resp.status_code)


# PUT
print(f'POST {apiUrl}')
resp = requests.put(
      f'{apiUrl}/5',
      json = {
          "author": "autor modificado"
      }
    )
print(resp.status_code)

