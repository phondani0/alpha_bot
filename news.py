from newsapi import NewsApiClient
import credentials as cred
import pprint
import stock_data_gatherer as sdg
import re
import util
import alpaca as alp


class NewsGetter:
    def __init__(self):
        self.api = NewsApiClient(api_key=cred.NEWS_API_KEY)
        self.alpaca = alp.Alpaca()

    def get_news(self, stock):
        asset = self.alpaca.get_asset(stock)
        print(asset)
        search_terms = stock + " " + \
            re.sub(r'[^\w\s]', '', asset)
        articles = self.api.get_everything(q=stock, qintitle=stock + " OR " + re.sub(
            r'[^\w\s]', '', asset), language='en', page_size=100)['articles']
        # qintitle=stock + " OR " + re.sub(r'[^\w\s]','',sdg.get_stock_company_name(stock))
        news_descriptions = []
        for news in articles:
            if util.check_overlap(search_terms, news['description']):
                # print(search_terms)
                # print(news['description'])
                news_descriptions.append(news['description'])
        return news_descriptions
