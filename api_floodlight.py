import http.client as httplib
import json


class StaticEntryPusher(object):

    def __init__(self, server):
        self.server = server

    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])

    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/staticentrypusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print
        ret
        conn.close()
        return ret


pusher = StaticEntryPusher('172.17.0.5')
with open("flows.json") as file:
    flows = json.load(file)

def short():
   pusher.set(flows['flows']['shortflow']['flow1'])
   pusher.set(flows['flows']['shortflow']['flow2'])


def long():
   pusher.set(flows['flows']['longflow']['flow1'])
   pusher.set(flows['flows']['longflow']['flow2'])
   pusher.set(flows['flows']['longflow']['flow3'])

short()
long()