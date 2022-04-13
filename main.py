from io import BytesIO
from flask import Flask,jsonify,request,json
import base64
from PIL import Image,ImageOps
from PIL import ImageEnhance
app = Flask(__name__)

@app.route('/enhance-image', methods=['GET','POST'])
def form_example():
    image = request.files['image']
    output_buffer = BytesIO()
    image1 = Image.open(image)
    #Mejorar brillo
    curr_bri = ImageEnhance.Brightness(image1)
    new_bri = 1
    img_brightened = curr_bri.enhance(new_bri)
    #Mejorar Color
    curr_col = ImageEnhance.Color(img_brightened)
    new_col = 2.5
    img_colored = curr_col.enhance(new_col)
    #Enhance Contrast
    curr_con = ImageEnhance.Contrast(img_colored)
    new_con = 0.5
    img_contrasted = curr_con.enhance(new_con)
    #Enhance Sharpness
    curr_sharp = ImageEnhance.Contrast(img_contrasted)
    new_sharp = 8.3
    img_sharped= curr_sharp.enhance(new_sharp)
    img_bws = ImageOps.grayscale(img_sharped)
    img_bws.save("Nueva_imagen.png")
    img_bws.save(output_buffer,format='PNG')
    byte_data = output_buffer.getvalue()
    base64_str=base64.b64encode(byte_data)
    str1 = base64_str.decode('utf-8')
    return json.dumps({'image':str1})
    

if __name__ == "__main__":
    app.run()