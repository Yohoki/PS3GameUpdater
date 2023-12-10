import requests
import pyperclip
import re

def CheckID(ID):
    #dirty Regex match check
    Reg = r"[A-Z]{4}[\d]{5}"
    ID = ID.upper()
    if (re.search(Reg,ID) == None):
        print("Invalid game ID. Please insert an ID.")
        return CheckID(input())
    return ID
def FetchXML():
    # Get the ID from the clipboard
    ID = pyperclip.paste()
    print(f"ID:{ID}")
    # Check if the ID is not empty
    if ID:
        ID = CheckID(ID)
        # Generate the URL
        url = f"https://a0.ww.np.dl.playstation.net/tpl/np/{ID}/{ID}-ver.xml"
        print(f"URL:{url}")
        try:
            # Fetch the XML content
            response = requests.get(url, verify=False)
            response.raise_for_status()  # Raise an exception for bad responses
            # Get the XML content
            xml_content = response.text
            # Copy the XML content to the clipboard
            pyperclip.copy(xml_content)
            print(f"XML content successfully fetched and copied to clipboard for ID: {ID}")
            print("Download URLs can be automatically added to JDownloader.")
        except requests.RequestException as e:
            print(f"Error fetching XML: {e}")
    else:
        print("Clipboard is empty. Please copy an ID.")
# Call the function to generate and fetch the XML
FetchXML()
