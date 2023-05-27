import pyshorteners
URL= input("Enter the URL: ")
a = pyshorteners.Shortener()
shorten_url = a.tinyurl.short(URL)
print("The Shortened URL is: " + shorten_url)