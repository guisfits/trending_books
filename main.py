from pytrends.request import TrendReq
import pandas as pd                        
from urllib.parse import urlparse, parse_qs

pytrend = TrendReq()
df = pytrend.today_searches(pn='BR')

trends_list = df.values.tolist()
trends_terms = [parse_qs(urlparse(url).query)['q'][0] for url in trends_list]


print(trends_terms)
