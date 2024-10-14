import os, sys
from PIL import Image
from jinja2 import Template

with open('xlsxart.template') as f:
    source = f.read()

XimgTemplate = Template(source)
im = Image.open("sample.png")
mx, my = im.size
pix = im.load()

def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor

rows = []
styles = {}

for y in range(my):
    row = []
    for x in range(mx):
        color = RGBToHTMLColor(pix[x, y])
        styles[color] = {'name': color, 'color': color}
        cell = {'style_name': color}
        row.append(cell)
    rows.append(row)

output = XimgTemplate.render(color_styles=styles.values(), rows=rows, imagesize={'x': mx, 'y': my})

with open('output.xml', 'w') as f:
    f.write(output)

print("Output saved to output.xml")