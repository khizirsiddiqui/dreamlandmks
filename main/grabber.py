#######################################################################
# grabber.py
# coded by: Nootan Ghimire <nootan.ghimire@gmail.com>
# description: Grabs Facebook Profile Pictures..
# Rather than a exploit, it is a service given by fb :D
#######################################################################

import urllib.request
from urllib.error import HTTPError, URLError


# Function that downloads a file
def downloadFile(file_name, file_mode, base_url):
    # Create the url
    url = base_url + file_name + "/picture"

    # Open the url
    try:
        f = urllib.request.urlopen(url)
        print("downloading ", url)

        # Open our local file for writing
        local_file = open(file_name + ".jpg", "w" + file_mode)
        local_file.write(f.read())
        local_file.close()

    # Handle errors
    except HTTPError as e:
        print("HTTP Error:", e.code, url)
    except URLError as e:
        print("URL Error:", e.reason, url)

# End Function

profile = 100000425733973  # Start From Profile ID

# Iterate over image range . Infinite Loop :)
while(1 == 1):
    base_url = 'https://graph.facebook.com/'
    s_index = str(profile)
    file_name = s_index
    # Now download the image. b for binary
    downloadFile(file_name, "b", base_url)
    profile = profile + 1
# End While Loop
# End Program
