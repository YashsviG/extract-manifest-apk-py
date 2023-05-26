from apkutils import APK
import os
import re

files = os.listdir("APKSamples/")
print(files)
paths = []
for file in files:
    filePath = f"APKSamples/{file}"
    fileName = re.sub('.apk', '', file)

    print("-----------------------------------------------------------")
    print(f"Extracting AndroidManifest.xml of:: {fileName}")


    apk = APK.from_file(filePath).parse_resouce()
    xmlGenerated = apk.get_manifest()
    
    file_obj = open(f'GeneratedXML/AndroidManifest-{fileName}.xml', 'w')
    file_obj.write(xmlGenerated)
    file_obj.close()
    
    print(f"Extraction completed, {file_obj.name}")
    print("-----------------------------------------------------------")

