from base_selenium_element import Elements, Element


class HomeElements(Elements):

    def __init__(self):
        # login
        self.open_login = Element('#LoginLink')
        self.email = Element('#page_email')
        self.password = Element('#page_password')
        self.login = Element('#LoginPageButton')

        # logout
        self.logout = Element('input[name="logout"]')

        self.search_box = Element('#searchString')
        self.search = Element('button[value="Search"]')
        self.search_results_heading = Element('h1[class*="search-results"]')

        self.open_watchlist_dropdown = Element('#SiteHeader_SiteTabs_BarOfSearch_watchlistDropdownOpen')
        self.view_watchlist = Element('#viewWatchlistDropDownLink')
        self.watchlist_dropdown = Element('#watchlist-toggle-extension-line')

        self.main_category = Element('#main-box-categories')
        self.main_categories = Element('#main-box-categories li a')
        self.subcategory = Element('#CategoryNavigator_CategoryPlaceholder')
        self.subcategories = Element('#CategoryNavigator_CategoryPlaceholder li a')
