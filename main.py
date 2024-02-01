from pytrends.request import TrendReq
import itertools

tzBR='-180'
pytrend = TrendReq(hl='en-US', tz=tzBR, timeout=(10,25))

df = pytrend.trending_searches(pn='brazil')
kw_list = list(itertools.chain.from_iterable(df.values.tolist()))
print(kw_list)

# book_category='22'
# geo='BR'
# last_week='now 7-d'

# pytrend.build_payload(kw_list, cat=book_category, timeframe=last_week, geo=geo)
# trends = pytrend.

# print(trends)
