from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import cv2 as cv
import urllib
import base64  


app = Flask(__name__)  

@app.route("/index", methods=["POST", "GET"])
def index():
    if 'error' in request.args:
        error = request.args['error']
    else:
        error = ''
    
    print(error)
    return render_template('qr_code.html', error=error)


@app.route("/bridge", methods=["POST", "GET"])
def bridge():
    if 'error' in request.args:
        error = request.args['error']
    else:
        error = '' 
    return redirect(url_for("index", error=error))
    # return ('', 204)


@app.route("/result", methods=["POST", "GET"])
def result(): 
    if request.method == "POST":  
        try: 
            print(request.files)
            print(request.form)   
            if request.form["qr_img_url"]: 
                qr_img_url = request.form["qr_img_url"]     
                try: 
                    url_response = urllib.request.urlopen(qr_img_url)
                    qr_img = np.array(bytearray(url_response.read()), dtype=np.uint8) 
                except:
                    error = "url is not an image"
                    return redirect(url_for("bridge", error=error))


            elif "qr_file" in request.files: 
                qr_img = request.files["qr_file"]#.read() 
                print(type(qr_img)) 
                qr_img = np.fromfile(qr_img, np.uint8)  

            else:  
                error = "no idea" 
                return redirect(url_for("bridge", error=error))

            if len(qr_img) > 0:
                qr_decode_img = cv.imdecode(qr_img, cv.IMREAD_COLOR)
                qr_img = base64.b64encode(qr_img) 
                res = cv.QRCodeDetector().detectAndDecode(qr_decode_img)  
                if res[0]: 
                    return render_template("qr_url.html", url=res[0], qr_img=qr_img.decode('utf-8')) 

            error = "image is not a QR code."
            return redirect(url_for("bridge", error=error))

        except Exception as e:
            error = 'try catch'
            return redirect(url_for("bridge", error=error))


# if __name__ == "__main__": 
#     app.run(debug=True)
