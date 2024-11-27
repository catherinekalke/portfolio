
import urllib

def read_text():
    quotes = open("/Users/catherinekalke/Documents/Income Tax/CRA NR6 2016 cover letter.docx")
    contents_of_file = 	quotes.read()
    print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)	

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
		print ("Profanity Alert!!!")
	elif "false" in output:
	    print ("No Profanity!")	
	else:
		print ("Could not open the document properly")
	print output
	connection.close()

read_text()	