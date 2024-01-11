import os
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import ssl
from werkzeug.serving import run_simple
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# # Load your private key and certificate
# context.load_cert_chain(r'C:\Users\gilos\cardcom\fullchain.pem', r'C:\Users\gilos\cardcom\privkey.pem')

#     # Optional: Set up ciphers
# ciphers = (
#     'DHE-RSA-AES256-GCM-SHA384:'
#     'DHE-RSA-AES128-GCM-SHA256:'
#     'ECDHE-ECDSA-AES256-GCM-SHA384:'
#     'ECDHE-ECDSA-AES128-GCM-SHA256'
# )
# context.set_ciphers(ciphers)

# # Disable older protocols
# context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/portraits')
def portraits():  # put application's code here
    image_folder = os.path.join(app.static_folder, 'resources/Portraits/')
    image_files = [os.path.join('/resources/Portraits/', image) for image in os.listdir(image_folder) if image.endswith((".png", ".jpg", ".jpeg", ".gif"))]
    print(image_files)
    return render_template('portraits.html', images=image_files)

@app.route('/misc')
def misc():  # put application's code here
    image_folder = os.path.join(app.static_folder, 'resources/Misc/')
    image_files = [os.path.join('/resources/Misc/', image) for image in os.listdir(image_folder) if image.endswith((".png", ".jpg", ".jpeg", ".gif"))]
    print(image_files)
    return render_template('misc.html', images=image_files)

@app.route('/maps')
def maps():  # put application's code here
    image_folder = os.path.join(app.static_folder, 'resources/Maps/')
    image_files = [os.path.join('/resources/Maps/', image) for image in os.listdir(image_folder) if image.endswith((".png", ".jpg", ".jpeg", ".gif"))]
    print(image_files)
    return render_template('maps.html', images=image_files)
if __name__ == '__main__':
    run_simple('0.0.0.0',443, app) #,  ssl_context=context)
