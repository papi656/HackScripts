# HackScripts

## script.py

## Dependencies
- requests

`pip install requests`
- BeautifulSoup

`pip install beautifulsoup4`

It downloads all the videos of series from [Index of series](http://dl.sv-mov.in/series/)

>For example, if you need to download Silicon Valley

`python script.py -l http://dl.sv-mov.in/series/silicon-valley/`

>the argument is the link of the page displaying links for all the videos

### Arguments
- ` -l or --link`
link for the required series
- ` -s or --season (optional)`
season number if you need to download specific season

> For example, if your need to download only the season 2 of Silicon Valley

`python script.py -l http://dl.sv-mov.in/series/silicon-valley/ -s 2`

### Improvements needed
  - Size of file already downloaded is printed everytime a new chunk of data comes, this need to be changed. Probably displayed every few seconds or a progress bar would be even better
  - Scripts does not check if some of the videos are already existing. So if for some reason the scripts is interrupted, it again starts downloading from the start without checking if those videos already exist
  - Many more changes needs to be done as this script was written on a lazy evening when I was lazy enough to not click each link once to download each video file. But that laziness was not enough to prevent me from writing this script which indeed took more hours.
