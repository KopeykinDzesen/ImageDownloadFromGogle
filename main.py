import requests
from bs4 import BeautifulSoup
from sys import argv

# script, url = argv

# мухомор
url = "https://www.google.by/search?client=ubuntu&hs=DWv&biw=1181&bih=542" \
      "&tbm=isch&sa=1&ei=kFxHWt7_IYP9kwWip5ToCg&q=%D0%BC%D1%83%D1%85%D0%B" \
      "E%D0%BC%D0%BE%D1%80&oq=%D0%BC%D1%83%D1%85%D0%BE%D0%BC%D0%BE%D1%80&gs" \
      "_l=psy-ab.3..0j0i67k1j0l8.37474.45421.0.45673.15.10.3.2.2.0.471.111" \
      "5.7j0j1j0j1.10.0....0...1c.1.64.psy-ab..0.13.1090.0..0i10i1k1.64.x21oU1A19yE"

# боровик
# url = "https://www.google.by/search?q=%D0%B1%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D0%BA&" \
#       "client=ubuntu&hs=sqa&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjO_MigtrHYAhUFyaQKHTYQDAkQ" \
#       "_AUICigB&biw=1181&bih=542&dpr=1.63"

def download_image():

    sourse_code = requests.get(url)
    soup = BeautifulSoup(sourse_code.text)

    images = soup.findAll(name="img", attrs={
        "alt": "Image result for мухомор"})

    for img in images:
        print(img["src"])


download_image()
