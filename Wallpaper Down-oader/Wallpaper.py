from selenium import webdriver
import requests, os
print "**************************** Welcome to Wallpaper downloader ****************************"
N = int(raw_input("Please Enter the number of Wallpapers you wish to Dounload :>>"))
loc = raw_input("Enter Download location")
try:
    brow = webdriver.Firefox()
except Exception in exc:
    print "Firefox needed, to perform operation"
url = "https://www.pexels.com/search/HD%20wallpaper"
brow.get(url)
photo_urls = []
photo_name = []
while(len(photo_urls) < N):
    photo_urls = []
    photo_name = []
    brow.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elems = brow.find_elements_by_css_selector(".photo-item img")
    for x in elems:
        src = x.get_attribute("src")
        src = src[:src.find('?')]
        name = x.get_attribute("alt")
        name = name[:20]
        photo_name.append(name)
        photo_urls.append(src)
        if(len(photo_urls) == N):
            break

brow.quit()
os.chdir(loc)

for i in range(len(photo_urls)):
    try:
        image = requests.get(photo_urls[i], verify = False)
    except Exception in exc:
        print "Could Not Connect to Internet, Please check connection and try again"
    file_name = photo_name[i]
    write_in = open(file_name+".jpg", 'wb')
    for j in image.iter_content(100000):
        write_in.write(j)
    write_in.close()
