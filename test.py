import requests

# url = 'http://localhost:8081/predict'
url = 'http://a02220565960d4b9795117efd412821a-2086114862.ap-southeast-1.elb.amazonaws.com/predict'

data = {'url': 'https://www.thehempshop.co.uk/media/catalog/product/cache/53255479565ca60bd805cf968bff78ae/b/l/blue_tshirt_7.jpg.mst.webp'}

try:
    result = requests.post(url, json=data).json()
    print(result)
except:
    print('error')