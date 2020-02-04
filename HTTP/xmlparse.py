import xml.etree.ElementTree as ET
import requests

source = "https://raw.githubusercontent.com/devdattakulkarni/elements-of-web-programming/master/data/austin-pool-timings.xml"

data = requests.get(source)

root = ET.fromstring(data.text)

for pool in root.findall('row'):
    pool_name = ''
    weekday = ''
    pool_type = ''
    weekday_closure = ''
    try:
        pool_name = pool.find('pool_name').text
        weekday = pool.find('weekday').text
        pool_type = pool.find ('pool_type').text
        weekday_closure = pool.find('weekday_closure').text
    except AttributeError:
        continue 
    print(pool_name, " ", weekday, " ", pool_type, " ", weekday_closure)


