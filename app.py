from flask import Flask, jsonify, request

import requests
import json
app = Flask(__name__)



@app.route('/verifyVP', methods=['POST'])
def verify_vp():

    
    vp = request.json

    vp=json.loads(vp)
    
    presentation = {'presentation':""}
    print(request.json)
    presentation["presentation"]=vp
    print(presentation)
    url = 'http://localhost:3332/agent/verifyPresentation'
    headers = {
        'Authorization': 'Bearer test123',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=presentation)
    if response.status_code == requests.codes.ok:
        response_data = response.json()
        # Do something with the response data
        print(response_data)
    else:
        print(f'Request failed with status code {response.status_code}')

    
    return response_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
