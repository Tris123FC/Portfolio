# 2. Analysis of Tech Sector Stock Market: 2014 - 2024

## **Motivation:**
The tech industry plays a crucial role in the global economy, and I wanted to explore how market trends impact the stock prices of major tech companies like Facebook, Google, Amazon, and Microsoft. This project involves a detailed analysis of stock price movements over time, with a focus on identifying patterns and factors influencing these trend. I then proceed to test the predictions of an LSTM machine learning model on future stock prices by comparing the prediction with the actual values of stock prices. The goal is to provide insights that could guide investment decisions and create a deeper understanding of the tech market landscape.

- **Data Source:** [Yahoo Finance - Markets](https://finance.yahoo.com/markets/)

- **Python File Link:** [Stock Analysis](https://github.com/Tris123FC/Portfolio/blob/main/2_stock_analysis/tech-sector-analysis-2024.ipynb)

## **Snapshot from project**
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/e2e24b53-ee51-4495-8348-5284766194cd">


## **Topic Introduction**

We all hear about the the stock market from time to time, whether we like it or not, especially when things turn to the red, always causing a feeling of dread as the news coverage switches towards the financial coverage of the day as, let's face it, it is never good news.A constant cycle of of peaks and troughs lead by investor sentiment and market speculation. Turning our lense towards the Tech-Sector financial stocks, will we see the same trends as described previously?

For this analysis I picked four stocks: Microsoft(MSFT), Amazon(AMZN), Apple(AAPL), Google(GOOG). I selected these stocks because they are all large multinational tech-companies that have branched out to offer multiple products and services.

## **Closing Stock Prices of 4 Big Tech Firms:**

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/36f7d004-1b09-4703-9738-9630fc0756a8">

This chart displays the daily adjusted closing price of stocks for a period of 1 year ending in September 2024.
The first thing we can spot is that Amazon, Google, and Apple have relatively similar stock prices, with Apple being slightly higher. In the third quarter of that year Apple had a stock price between 200 and 250, while Amazon and Google had a stock price between 150 and 200. The closeness in stock prices might suggests these companies are direct competitors for stock market investment. Microsoft, however, has a much higher stock price with an adjusted stock price almost always above 400 for the same period. This might be due to the type of product and services that each company provides. If we compore two companies, Apple is most well known for its user friendly technology products, while Microsoft is better known for its software business.

One addition thing to note is the dip between  June and July. Articles from Investopedia suggest the reason might be due to a mix of investor rotation, interest rate speculation about potential interest rate cuts, and earning disappointement from underwhelming earning reports. You can see the dip clearer in the charts below.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d69f8225-862f-4836-ac48-ff3e57435626">


Further insights into stock market performance can be found by looking at the stock market price moving average.

## **Stock Market Moving Average**

What is a moving average?

A moving average is calculated by taking the mean of a given set of values over a specified period.

In financial analysis, the moving average is a key indicator it is used to:

- smooth out the price data by creating a constant moving average.
- Identify the direction of the stock

You decide on the how short or long the moving average based on the purpose of your analysis.
Shorter moving averages are used as indicators for short term trading, while longer moving averages is for more long term investment.


<img width="1000" alt="image" src="https://github.com/user-attachments/assets/8ca19649-f645-491f-96cc-04f6fe2739db">

Looking at the moving average chart, we can see that although there was a dip in June and July the moving average has been constantly increasing over that period, suggesting a strong belief among investors in the tech industry as prices are still higher on average.

As we now have a better understanding of stock market price trends, let's look further into investment returns.

## **Analysis of Daily Investment Returns**

Daily returns is the percentage change in stock prices. This measure is used to show the volatility in the stocks.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d6bd86cf-7637-458c-b7be-aaea88f2e7e5">

A general rule of thumb for stocks is the 1%-2% rule. Stocks within those ranges are considered volatile. Based on this rule, we can see that tech stocks are relatively stable compared to other more volatile stocks.
We can quickly see that the percentage daily returns moves around the 0% mark. Amazon and Google have a slightly wider variation range, but changes generally don't go past the 0.1% mark.

We can get a better sense of volatility by looking at the distributions of daily returns for each companies' stock.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/0629cfc3-c415-4a58-a671-9358d19f9c8f">

From the distribution charts, we can see that each stock appears in roughly normally distributed with a low variance centred around 0 with a few extreme daily returns rates as a result of market fluctuations.

We see from our previous analysis that all companies share identical trends, a correlation analysis might offer suggestions on the relations between each stock.

## **Correlation Relations between Tech Companies**

Correlations coffeficients is a measure of the statistical relations between two variables, assuming there is some kind of linearity in the relationship.
Two variables have a positive correlation if an increase in one variable leads to an increase in the other.
A strong positive correlation is in the range between 0.5 and 1, a strong negative correlation is between the range of -0.5 and -1.
Below is a correlation heat map for the 4 tech stocks that we selected:

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/095b8cb0-312e-42b0-8d24-ba7615e79fcc">

There are positive correlations between each stock suggesting stock performance is affected by common factors. Factors might include things such as stock market speculation, and investor sentiment.

So far we have identified similar trends in the stocks, and we have identified strong positive correlations between each stocks. Would these similarities be releflected in the the risk attributed to each stock?

We can give a risk assessment by plotting a chart of the daily returns mean (expected returns) and standard deviation (risk).

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/5ae2c64c-f8ba-495a-9454-4aa6dd012d27">

Overall each Tech stock is relatively low risk with low returns. This is because the stocks are well-established with a good reputation. However when comparing the four we can see that Apple is the best stock to invest in as it is low risk with better expected returns. Google on the otherhand is the the least attractive as in as it has higher risk and low expected returns.

We have looked at all the current data on those four stocks, and have identified the similarities in trends, relations, risk and exptected returns, but we have very little knowledge about how these stocks will evolve in the future. Future information would be extremely useful as it could guide us in making investment decisions. Unfortunately, it is impossible to predict the future, many people have tried and failed, but we can still give it our best shot using knowledge of machine learning.

## **Applying Machine Learning to Stock Data**

Machine learning can be described as the process which computer programs go through to learn how to process data to hopefully produce a correct ouput. It involves a whole lot of Maths functions and a huge variety of algorithms to pick from, but in simple terms, the idea of machine learning is to minimise a loss function which represents the difference between the actual value and the predicted  value. Luckily for us, we can skip the Math and algorithm parts of applying machine learning, as frameworks have already been established and they are freely available to use. For this section we will use Keras, a framewwork developed by programmers to faciliate machine learning applications.

We aim to use historical data to predict closing prices, so we need some kind of regression model.

I chose to use the LSTM (Long Short Term Memory) model, which is effective in predicted values based long term time-series data. This model analyses multidimensional test data in sequences, gradually reducing the complexity until it finds the best regression model.

The first visulisation shows a wide view of the model predictions based on 10 years of data. We can see thatthe model did quite a good job at fitting the values with its predictions.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/0fc13dd0-f065-49db-b56f-cfea36024574">

Zooming in, we see that there is still a significant margin of error. This model can be used to gain an overall sense of market trends, but it should not be used to predict exact prices.

<img width="478" alt="image" src="https://github.com/user-attachments/assets/00ea1e8e-1216-43fb-9047-25fdcab6557b">

## **Summary**

From our analysis of some of the biggest tech companies, we found similarities among them:
- Each experience June-July market dip, likely caused by investor rotation, market speculation, and disappointing earnings.
- There moving average prices continually increased over the one year period, suggesting a strong and steady tech sector.
- There were ositive correlations between each stock, possibly due to common factors are influencing stock prices.
- Overall each of the stock were Low risk with low expected return for each stock as they are considered relatively safe.
  
All of these finding show similarities in trends, relations, risk and exptected returns.

We then proceeded to try and predict future data using machine learning and LSTM modelling.
- The generated regression model was able to accurately predict the overall trends of the markets.
- However, there is still a significant margin of error, which makes it unsuitable for predicting prices and making investment decisions.
- Further refining of the model would lead to more accurate price predictions.



