import time
#we need to import time modele so that we run the program after some time
import urllib.error

# we also need to import urllib.error so that we get to know what type of error
import urllib.request
#we finally need to import urllib.request so that we can open the URL

def check_url(my_website):
    #we use while loop in order to keep running the program
    while True:
        try:
            connection = urllib.request.urlopen(my_website)
            #accessing the connection
        except urllib.error.HTTPError as e:
            #if there is HTTP error
            print(f'HTTP error: {e.code} for URL: {my_website}')
        except urllib.error.URLError as e:
            #if there was URL not opening error
            print(f'URL error: {e.code} for URL: {my_website}')
        else:
            #otherwise, there is no error
            print(f'Your website is: {my_website}\n I assure it up to date')
            print(" ")
        time.sleep(60)
        #then wait for 1 min

if __name__ == '__main__':
    url = "https://jndayisenga-portfolio.netlify.app"
    check_url(url)
