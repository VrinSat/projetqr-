# basic_qrcode.py

import segno

qrcode = segno.make_qr("ça marche enfin") 
qrcode_rotated = qrcode.to_pil(
    scale=5,
    border=2,
    dark="darkblue",
    quiet_zone="blue",
    data_dark="red",
    data_light="lightblue",   
).rotate(45, expand=True)
qrcode_rotated.save("formatted_rotated_qrcode.png")
