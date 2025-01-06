#this is a lot like scraping data 
with open('emails.txt','r') as emails:
    emails = emails.readlines()
    
for email in emails:
    #print("look for hotmail account")
    if "gmail" in email:
        print(email.rstrip())
#rstrip gets rid of newline tags
