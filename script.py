from bs4 import BeautifulSoup as beauty
import requests
import os
import sys
import argparse 

def getting_url():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--season", help="If you need to download only specific season", action="store")
    parser.add_argument("-l", "--link", help="The path of the series", action="store")
    args = parser.parse_args()
    r = requests.get(args.link)
    soup = beauty(r.content, 'html.parser')
    links = soup.find_all("a")
    urls = []
    if args.season:
        season = 'S0' + args.season
        for i in range(len(links)):
            val = links[i]['href']
            if '.mkv' and season in val:
                urls.append(args.link + val)
    else: 
        for i in range(len(links)):
            val = links[i]['href']
            if '.mkv' in val:
                urls.append(args.link + val)
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
        fileName = download_file(urls[i])
        print (fileName, " Downloaded\n")

if __name__ == "__main__":
    main()


