#Downloads back catalogue of Grauniad Cryptic Crosswords

#imports
import pdfkit
import os.path
import urllib.request
import time

# init some vars
version = "0,1"
choice = 0
inputerror = "\n"

# loop until user enters an integer [or q/Q]
while True:

    choice = (input("\n\n==================================================\nGrauniad Cryptic Crosstie Scraper "+version+"\n==================================================\n\nWhich crossword do you want to download. Enter:\n\n1 –to download Guardian Quiptics\n2 –to download Guardian Cryptics\n3 –to download Observer Everyman Cryptics\nQ -to quit\n\n==================================================\n"+inputerror))

    # Quip
    if choice == "1":
        choiceshortstring = "quiptic"
        choicetext = "Guardian Quiptic"
        latestcrosstieurl = "https://www.theguardian.com/crosswords/series/quiptic/latest"
        break

    # Cryptic
    elif choice == "2":
        choiceshortstring = "cryptic"
        choicetext = "Guardian Cryptic"
        latestcrosstieurl = "https://www.theguardian.com/crosswords/series/cryptic/latest"
        break

    # Obbo
    elif choice == 3:
        choiceshortstring = "everyman"
        choicetext = "Observer Everyman"
        latestcrosstieurl = "https://www.theguardian.com/crosswords/series/everyman/latest"
        break

    # Quit
    elif choice == "q" or choice == "Q":
        print("Quitting. Bye!!!...")
        quit()

    #Invalid value entered. keep looping with error message
    else:
        inputerror = "ERROR: Choose 1,2,3 or Q!\n==================================================\n\n"


print("You chose to download "+choicetext)

#find number of current crossword
currentcrosstieurl = urllib.request.urlopen(latestcrosstieurl)
#above will redirect to URL of format https://www.theguardian.com/crosswords/<crossword choice>/XXXXX
#where XXXXX is the current one
urlreturned = currentcrosstieurl.geturl()
print("Latest "+choicetext+" is downloadable from: "+urlreturned)
#extract bit after last slash [ie. no.]
currentcrosstienumber = int(urlreturned.rsplit('/', 1)[-1])
print("Latest "+choicetext+" crossword is number: "+str(currentcrosstienumber))
#count back from that one
count = currentcrosstienumber
numberprinted = 0
numberfailed = 0

#savedir on desktop [make sure it exists]
savedir = os.path.join(os.path.expanduser('~'),'Desktop/'+choicetext)

#savedir doesn't exist. create it
if not os.path.exists(savedir):
    print("NOTICE: Creating destination directory: "+savedir)
    os.makedirs(savedir)
#savedir exists. Make sure we're OK to write to it
else:
    while True:
        shouldwecontinue = input("\n==================================================\nNOTICE: The crossties are going to be saved in: "+savedir+". However that directory already exists! Make sure you're not overwriting something important.\nContinue (Y) or Quit (Q) ?\n==================================================\n")
        if shouldwecontinue == "y" or shouldwecontinue == "Y":
            break
        elif shouldwecontinue == "q" or "shouldwecontinue" == "Q":
            print("Quitting. Bye!!!...")
            quit()
        else:
            print("Enter Y or Q!")

#time execution
starttime = time.clock()

#loop to print crossties
while (count > 0):

    #zeropad to 5 digits
    countasstring = str(count).zfill(5)

    #build filename
    filename = (choicetext+" "+countasstring+".pdf")

    #build savepath
    savepath = os.path.join(savedir,filename)

    #build URL to crosstie
    crosstieurl = "https://www.theguardian.com/crosswords/"+choiceshortstring+"/"+str(count)+"/print"

    #try getting that URL
    try:
        print("Printing "+choicetext+" no."+countasstring+"...")
        #save it as a PDF
        pdfkit.from_url(crosstieurl, savepath)
        numberprinted += 1
    except: #sommit went wrong
        print(choicetext+" "+countasstring+" doesn't exist, or save dir doesn't exist, or some other crap happened!")
        numberfailed += 1
    count = count - 1
    break

endtime = time.clock()
elapsedtime = round((endtime - starttime),2)
#print("time taken:\nStart time: "+str(starttime)+"\nEnd Time: "+str(endtime)+"\n===================\nTOTAL: "+str(endtime-starttime))
print("\n==================================================\nAW DUM! -- Files were saved to "+savepath.rsplit('/', 1)[0]+"\n"+str(numberprinted)+" crosswords were downloaded and converted to PDF in "+str(elapsedtime)+" seconds.\n"+str(numberfailed)+" crosswords failed to print.\nEnjoy!\n==================================================\n")

#TODO: more helpful error messages [fetching URLs and printing to PDF]. Don't overwrite existing crossties. 
