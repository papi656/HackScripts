from bs4 import BeautifulSoup as beauty
import requests
import os
import sys

def getting_url():
    r = requests.get(sys.argv[1])
    soup = beauty(r.content, 'html.parser')
    links = soup.find_all("a")
    urls = []
    for i in range(len(links)):
        val = links[i]['href']
        if '.mkv' in val:
            urls.append(val)
    return urls


def correct_name(name):
    newName = ""
    i = 0
    while i < len(name):
        if name[i] == '%':
            newName = newName + '_'
            i = i + 3
        else:
            newName = newName + name[i]
            i = i + 1
    return newName



def download_file(url):
    local_filename = url.split('/')[-1]
    cName = correct_name(local_filename)
    r = requests.get(url, stream=True)
    with open(cName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                #printing file size downloaded
                size = os.path.getsize(cName)
                print ("Downloaded %d MB"%(size/(1024*1024)))
    return cName

def main():
    urls = getting_url()
    for i in range(len(urls)):
        urlToDownload = sys.argv[1] + urls[i]
        fileName = download_file(urlToDownload)
        print (fileName, " Downloaded\n")

if __name__ == "__main__":
    main()


