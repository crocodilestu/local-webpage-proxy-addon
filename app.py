from flask import Flask, request, Response
import requests
import ssl

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = f"http://{request.host}/{path}"
    headers = dict(request.headers)
    headers['Host'] = request.host
    response = requests.get(url, headers=headers, stream=True, verify=False)
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in response.raw.headers.items() if name.lower() not in excluded_headers]
    return Response(response.content, response.status_code, headers)

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('/ssl/fullchain.pem', '/ssl/privkey.pem')
    app.run(host='0.0.0.0', ssl_context=context)
