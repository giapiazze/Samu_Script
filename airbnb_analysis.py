from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from airbnb_db import Base
import urllib.request
import http.client


def http_analysis(house, date):
    url_simple = 'https://www.airbnb.it'
    url = 'https://www.airbnb.it/rooms/' + house.airbnb_id + '?location=' + house.location + '&adults=' + \
          str(house.adults)
    conn = http.client.HTTPSConnection('www.airbnb.it')
    conn.request("GET", url_simple)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    print(mystr)

    a = 3


# """
# Function to execute the search
# :param folder: The folder to search in
# :type folder: string
# :param recursive: Recursive search
# :type folder: boolean
# :return: file name found
# :rtype: array
# """
