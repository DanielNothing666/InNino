from IPython.display import display
import pandas as pd
import numpy as np
from ipyleaflet import Map, Marker, FullScreenControl
from ipywebrtc import WidgetStream, ImageRecorder

c_lat,c_lon = 52.5917,39.5757
m = Map(center=(c_lat,c_lon),zoom = 15)
m.add_control(FullScreenControl())
#mark = Marker(location = (
widget_stream = WidgetStream(widget=m, max_fps=1)
image_recorder = ImageRecorder(stream = widget_stream)
display(image_recorder)
outfp = 'D:/NNTU/Folder/map.html'
m.save(outfp)
with open('D:/NNTU/mp.png', 'wb') as f:
    f.write(image_recorder.image.value)
