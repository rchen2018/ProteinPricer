# ProteinPricer
ProteinPricer is a python script that uses Selenium WebDriver to check the prices of the (objectively) best flavors of whey protein on the MyProtein website: Strawberry Cream, Salted Caramel, Chocolate Smooth, Vanilla, and Mint Chocolate Chip. MyProtein has "sales" nearly every week, so buying protein at retail price is overspending. Keeping track of the many different sales is tedious and time consuming - ProteinPricer's goal is to automate the process through web scraping and apply discount codes to caluclate the sales price. Every time the script is run, these prices are stored in a database and compared to other past prices. The script is run automatically every day at noon through python schedule (which can be turned off), and if the sales prices are below a certain threshold, an email or text alert will be sent.

Still a work in progress!!
