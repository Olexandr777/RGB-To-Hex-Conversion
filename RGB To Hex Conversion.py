def rgb(r, g, b):
    return f'{ min(max(r,0),255):02X}{min(max(g,0),255):02X}{min(max(b,0),255):02X}'
