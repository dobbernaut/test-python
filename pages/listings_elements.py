from base_selenium_element import Elements, Element


class ListingsElements(Elements):

    def __init__(self):
        self.total_listings = Element('#totalCount')
        self.all_listings = Element('div[data-listingid]:not([class*="no-listing"])')
        self.listings_add_to_watchlist = Element(
            'div[data-listingid]:not([class*="no-listing"]) div[class*="watchlist-corner"]')
        self.listings_title = Element('div[data-listingid]:not([class*="no-listing"]) div[class="title"]')
