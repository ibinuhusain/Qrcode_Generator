
import qrcode
from PIL import Image 
from pathlib import Path
import os

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def Take_Input():
    os.remove("image.png")
    os.remove("assets\image.png")
    text = entry.get("1.0", "end-1c")
    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("image.png")
    img_PIL = Image.open(r'image.png')
    img_PIL.save(r'assets\image.png')
    canvas.update()
    
   
    
    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("480x250")
window.configure(bg = "#E6CBCB")


canvas = Canvas(
    window,
    bg = "#E6CBCB",
    height = 480,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
button_1 = Button(
    text = "Generate",
    borderwidth=0,
    highlightthickness=0,
    command = lambda:Take_Input(),
    relief="flat"
)
button_1.place(
    x=270.0,
    y=180.0,
    width=80.0,
    height=20.0
)
entry_bg_1 = canvas.create_image(
    364.0,
    190.0,
)
entry = Text(
    bd=0,
    bg="#D6A8A8",
    highlightthickness=0
)
entry.place(
    x=200.0,
    y=100.0,
    width=250.0,
    height=50.0
)

canvas.create_text(
    204.0,
    37.0,
    anchor="nw",
    text="QR Code Generator",
    fill="#9F6363",
    font=("RubikOne Regular", 30 * -1)
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image.png"))
image_1 = canvas.create_image(
    100.0,
    140.0,
    image=image_image_1
)


window.resizable(False, False)
window.mainloop()
