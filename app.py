# app.py
import falcon
import json


class SubmitResource:
    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))
        value1 = int(data['value1'])
        value2 = int(data['value2'])
        value3 = int(data['value3'])
        value4 = int(data['value4'])
        result = value1 + value2 + value3 + value4
        # Store the result in some database or file
        resp.media = {'result': result}


class ViewResource:
    def on_get(self, req, resp):
        # Retrieve the result from the database or file
        # For simplicity, just return a placeholder value
        result = 100
        resp.media = {'result': result}


api = falcon.API()
api.add_route('/submit', SubmitResource())
api.add_route('/view', ViewResource())
