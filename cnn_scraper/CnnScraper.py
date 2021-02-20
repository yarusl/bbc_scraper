from Article import Article

class CnnScraper:
    def __init__(self, driver, topic_url, pages_to_scrape = 1):
        self.driver = driver
        self.topic_url = topic_url
        self.articles = [] # list of instances of class Article
        self.pages_to_scrape = pages_to_scrape
        self.validate_topic(topic_url)

    def validate_topic(self,topic_url):
        """ 
        checks if the topic is scrapable.
        meaning that the page has a 
        'Latest Updates' section.
        """

        #TODO MICHAEL -- look for latest-updates

        pass

    def scrape(self):
        """ 
        scrapes all the articles from 
        n-pages
        """
        #driver.page_source.encode("utf-8") -- reminder
        page = self.driver.get(self.topic_url)
        for p in self.pages_to_scrape:
            self.articles += self.scrape_latest_updates()
            #go to next page

        return self.articles

    def scrape_latest_updates(self):
        """ 
        scrapes all articles from 
        the 'Latest Updates' section
        """
        articles = []
        return articles

    def __str__(self):
        """ 
        returns a readable representation 
        of the result of the scrape 
        """
        pass

    def __del__(self):
        """ closes the browser """
        self.driver.quit()