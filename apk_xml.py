from tkinter import Tk
from tkinter.filedialog import askopenfilename
from apkutils import APK

Tk().withdraw()
filePath = askopenfilename()

name = filePath.split("/")
fileName = name[-1].split(".")[0]

apk = APK.from_file(filePath).parse_resouce()

xmlGenerated = apk.get_manifest()
file_obj = open(f'GeneratedXML/AndroidManifest-{fileName}.xml', 'w')
file_obj.write(xmlGenerated)
