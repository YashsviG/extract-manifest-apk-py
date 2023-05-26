## Extracting Android Manifest from APK - Python

### Library Used: apkutils 
https://github.com/kin9-0rz/apkutils/tree/master 

### How to run the script
1. Download the code or fork the repo and do a git clone.
2. IF Python and pip are not installed already: <br/>
2.1. Go To: https://www.python.org/downloads/ to download latest Python. <br/>
2.2. Follow: https://www.geeksforgeeks.org/download-and-install-pip-latest-version/ <br/>
2.3 Drop APK files in the APKSamples directory to extract AndroidManifest.xml from
3. In the terminal run: `pip install -r requirements.txt` to install all the needed libraries.
4. Run `python3 apk_xml.py` in the terminal --> this will allow you to select an APK file from file explorer and would generate an XML file in the GeneratedXML folder.

> Note: There has been an APK file provided in the APKSamples directory.

### Sample demo video
https://github.com/YashsviG/extract-manifest-apk-py/assets/45160510/f82e5c16-3043-47fc-a5d6-89c28244e8a7

