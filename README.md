![](headerimage.jpg)

# Grauniad Cryptic Crosstie Scraper #

This is just a quick hacky script I wrote to grab back issues of The Guardian newspaper's various cryptic crosswords and save them [in PDF format] into a folder on your desktop. 

The Guardian is rare amongst newspapers in allowing free access to its entire back catalogue of crosswords. It also provides three series of cryptic crosswords, spanning a nice range of difficulty; The Quiptic --which is fairly easy, The Observer Everyman --which is somewhere in the middle and the Guardian Cryptic --which can be quite tough.

This script allows you to download either [or all] of those three archives.

### Prerequisites ###

* Python 3. Will need tweaking to run on Python 2,x
* PDFkit [for saving the crosswords as PDFs]. Install with `pip3 install pdfkit`
* Internet connection [duh!]
* Lots of patience. \[See notes below on speed\]

### Usage ###

* `python3 GrauniadCrosstieScraper.py` --and answer the questions on-screen
* To quit it before it's finished you'll have to interrupt it with `CTRL+C` [I told you it was clunky!]

As I just knocked this up for my own benefit, it's not very sophisticated; there's next to no error-checking and the file-naming and file-saving location are hard-wired in.  But it gets the job done and is a lot less hassle than manually incrementing a URL and printing the resultant page to PDF eleventy-billion times in a row. That said, the script is extremely s-l-o-o-o-w. Grabbing the actual URLs is quick enough but PDFkit takes several seconds to process each one.  So, given that and the fact that I've not yet implemented limiting the download to a custom range, this is best deployed as one of those things you set running and then go off and do something else for several hours.

Pull requests welcome, if you want to tidy it up a bit. Doing anything much else with it is not high on my list of priorities, as it was a quick hack, which has now served its purpose. 
