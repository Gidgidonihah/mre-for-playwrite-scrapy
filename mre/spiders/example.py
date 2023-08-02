import scrapy


class ExampleSpider(scrapy.Spider):
    """A Minimum working example of meta-refresh failure."""

    name = "meta-refresh"

    def start_requests(self):
        url = "https://gidgidonihah.github.io/mre-for-playwrite-scrapy/"
        yield scrapy.Request(url, meta={"playwright": True})

    def parse(self, response, **kwargs):
        """Not needed because an error will be raised by playwright_scrapy."""
