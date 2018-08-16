### Rebalancing Citi BIke
## Summary:
This project is using Citi Bike dataset to predict the number of users for a bike station. The problem with bike stations is that users have to rebalance a bike station in order to meet demands. With my model, I can predict the number of users for a bike station given the bike station, date, and time. This will essentially help the Citi Bike rebalancing team to reduce the number of bikes being swapped between stations.

Citi Bike data set contains 1.5 million rows of bike ride data from start location to end location for the first 6 months of 2018. 

Mapped Citi Bike stations with MTA stations to identify demand complementarity across means of transportation using Google maps and geolocation API tools.

## Tools Used:
Linear Regression, Random Forest, and CatBoost
Git
Web Scraping/BeautifulSoup
Pyhton/Pandas/numpy
Google Maps API 


## Future:
- Explore target variables which are skewed to the right. Cause model to overfit on bike station with low number of users. 
-Increase to a larger dataset using Spark. 
-Combine with dockless bike dataset to investigate where people are dropping and picking up bikes. This could provide insights on where to place the new dock stations. 
