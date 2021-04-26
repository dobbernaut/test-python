from base_selenium_element import Elements, Element


class WatchlistElements(Elements):

    def __init__(self):
        self.delete = Element('input[value="Delete"]')
        self.confirm_deletion = Element('#submit1')
        self.cancel_deletion = Element('#cancel')

        self.watchlist_form = Element('form[action*="Watchlist"][method*=get]')
        self.listings_checkbox = Element('td[align="center"] input[type="checkbox"]:not([id*="cmdSelect"])')
