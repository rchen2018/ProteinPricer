# ProteinPricer
ProteinPricer uses Selenium WebDriver to check the prices of the (objectively!) best flavors of whey protein on the MyProtein website: Strawberry Cream, Salted Caramel, Chocolate Smooth, Vanilla, and Mint Chocolate Chip. MyProtein has "sales" nearly every week, so buying protein at retail price is overspending. Keeping track of the many different sales is tedious and time consuming - ProteinPricer's goal is to automate the process and apply discount codes to caluclate the sale price. Every time the script is run, these prices are stored in a SQLite database and compared to past prices of the same flavor so the user can easily decide if the current price is a good deal.

Still a work in progress!!
