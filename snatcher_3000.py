from requests_html import HTMLSession

session = HTMLSession()

URL = 'https://www.nvidia.com/en-us/shop/geforce/gpu/?page=1&limit=9&locale=en-us&category=GPU&gpu=RTX%203080'

page = session.get(URL)

page.html.render()

print(page.html.search('Out Of Stock'))