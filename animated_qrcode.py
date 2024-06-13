import segno

from urllib.request import urlopen 
slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=gN9S70XduZ8")
gif_url = urlopen("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmxxczlpY3kwb25tbzl5N2VnM2U0NTY5ZHZncm84Y3Bxbmx2cW5jcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8c1SH3KQGyWOBa9XvK/giphy.gif")
slts_qrcode.to_artistic(
    background=gif_url,
    target="animated_qrcode.gif",
    scale=5,
)
