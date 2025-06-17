from rembg import remove
from PIL import Image
from io import BytesIO
 
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def background_img_remove(uploaded_img):
    image=Image.open(uploaded_img)
    fixed=remove(image)
    op=convert_image(fixed)
    return op