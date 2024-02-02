from pytrends.request import TrendReq
import itertools

def get_trends():
    tzBR='-180'
    pytrend = TrendReq(hl='en-US', tz=tzBR, timeout=(10,25))

    df = pytrend.trending_searches(pn='brazil')
    list_of_trends = df.values.tolist()
    trends = list(itertools.chain.from_iterable(list_of_trends))

    return trends
