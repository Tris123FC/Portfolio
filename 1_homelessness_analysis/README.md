# Analysis of Homelessness Relief Figures (2024)
## **Motivation:** 

Homelessness is a pressing social issue, and I wanted to understand how government spending impacts homelessness rates across different regions. This project involves a time-series analysis of relief spending relative to housing procurement and a geographical analysis of homelessness figures across the England. The goal was to identify trends and disparities that could inform policy decisions.

- **OneDrive Link:**
  [Access Excel File](https://onedrive.live.com/personal/c88ea4021b131a70/_layouts/15/Doc.aspx?resid=C88EA4021B131A70!s3cdfa7f6c7ef427a8df49b9f1452d4e3&cid=c88ea4021b131a70&migratedtospo=true&app=Excel)

- **Data Source:**
  
  [UK GOV - Statutory Homleness - 2024](https://www.gov.uk/government/statistical-data-sets/live-tables-on-homelessness)
  
  [ONS GOV UK - Inflation and Price Indices - 2024](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/costoflivinginsights/food)
  
  [Nationwide - House Price Index - 2024](https://www.nationwidehousepriceindex.co.uk/resources/f/uk-data-series)

  

## **Project Snapshot:**

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/d125a904-968a-44b7-a5ff-cd83e6f8bdbd">



## **Homlessness Rates Across England**

With a new Labour Party government recently elected, building homes is at the top of the agenda as property prices and living costs skyrocket,
all of this is in an effort to reduce purchase and rental costs with intent to alleviate the burden of English residents. Below are two charts which show how estimates of average house prices
and inflation evolved over time.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d1016736-5ae7-45b6-bb34-9bcf9ea65737">


*UK house prices reached around £262,000 in 2024 compared to 181,000 in 2007.*

source: [Nationwide - House Price Index - 2024](https://www.nationwidehousepriceindex.co.uk/resources/f/uk-data-series)

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/f51a75eb-b88c-472f-9bf0-200b492bf6d4">

*January 2024 saw an inflation rate of 7%.*

source: [ONS GOV UK - Inflation and Price Indices - 2024](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/costoflivinginsights/food)

These two charts show the pressure that is being added onto UK residents because of rising housing costs and food costs.
It is fair to say that the new government has a hard job ahead of them, with the previous government failing to resolve the growing demand for houses.
But what about the people who are the most at risk?

## **Homelessness in the UK**
A 2024 report by the government dating back to August 2024 provides data on owed relief and homeless figures from the second quarter of 2018 to the first quarter of 2024.

Before we go further into the report, it is important to know that owed relief is the money assessed owed by the government to England residents who are threatened with homelessness or who are currently homeless. 
We use this measure as an estimate of government spending on homlessness prevention and relief.

By analysing the regional data, we can get a quick glimpse at the areas that are most affected by homelessness.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/83ec46bb-b0e4-4932-9f45-022c31641f84">

source: [UK GOV - Statutory Homleness - 2024](https://www.gov.uk/government/statistical-data-sets/live-tables-on-homelessness)

We can observe some disparity between regions. The North East is most affected by homelessness. By looking at the median house price to median residence earning ratio, we can see that this is not directly due to housing affordability.
A high ratio would suggest the price is higher relative to earnings, meaning housing is less affordable. 

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/f0d1a20b-b917-4d7a-87ad-806459fb083a">

source: [ONS GOV UK - House Prices to Growth Earnings Ratio](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/housepriceexistingdwellingstoresidencebasedearningsratio)

The North East has the lowest ratio which tells us there housing is more affordable than in other regions. This leaves us to deduce that disparities might be due to lack of access social care, family support, and government aid.

## **Spending on homelessness prevention and relief**

We selected the assessed total owed relief measure to represent government spending on prevention and relief. The tree map below shows the proportion of spending across regions.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/2fa174af-b927-4527-ac48-3d136a009823">

Again we see disparities in spending. London spent the most on relief and prevention with around 21% of total spending. The differences in spending is mainly due to population and cost of living differences across regions.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/acbb7f11-2246-4984-916b-1bdaa6a029a3">

As we can see from the chart the London has a population of around 9 million, comparable to the South East. Whilst, other regions are less populated, the North East holding a population of nearly 3 million.

source: [ONS GOV UK - Estimate of Population for England and Wales - 2024](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/estimatesofthepopulationforenglandandwales)

Cost of living disparities is best represented using the average private rent. Below is a chart that shows the average rent for private properties across England.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/9fdd8cb8-c76a-4370-a477-f14e017bb00a">

source: [ONS GOV UK - Private Rent and House Prices - 2024](https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/privaterentandhousepricesuk/august2024)

London has the highest private rent costs, meaning securing housing for individuals at risk is more expensive if there is not enough council housing.

While most of the disparities might be explained by differences in population and living costs, it would be safe to assume that social regional differences are key drivers for the disparity in unemployment rates.


From are previous analysis we can identify key insights on the geographic nature of homelessness.

- Different regions are affected more than others, the North East has the highest homeless rate at 0.22%

- Spending on prevention and relief measures is different across regions, mostly due to population and cost of living disparities, London and the South East being the most costly.

- This leads us to assume any disparity in homeless rates is due to social regional differences in access to care, family support and government relief.

Now that we better understand the most affected regions and the spending associated with each area, let's look at the demographics, specifically which age group is most likely to be at risk of homelessness.

## **Demographics of people at risk of homelessness**

Looking at the demographic distribution through a pie chart, gives us a clearer idea of which age group is more at risk of being homeless.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/a86d9459-da7b-40db-985f-996298736395">

source: [UK GOV - Statutory Homleness - 2024](https://www.gov.uk/government/statistical-data-sets/live-tables-on-homelessness)

As we see from the chart, the population most at risk is between the ages of 25 and 44. This is probably the result of higher unemployment rates among these age groups which reduces long run income stability 
and increases the risk of being homeless.

Below is a chart which displays the proportion of people unemployed by age group:

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/824b7f20-e66a-40f9-a99e-fa781d4cd860">

source: [Statista - Unemployement in the UK by age group](https://www.statista.com/statistics/974421/unemployment-rate-uk-by-age/)

The data confirms the assumption of higher unemployment rates among those groups.
The higher unemployment rates among people aged between 24 and 35 suggest some inequality in job opportunities between age groups.

This inequality might be explained by:

- poor economic performance, leaving employers unwilling to invest in new hires.
  
- a shift of work place culture towards remote work, with reduced demand for office based jobs.
  
- less opportunities for apprenticeship and traineeship as people work more and more from home.

## **Government initiatives to assist people at risk**

According to government policy, homelessness relief is the action taken to help resolve homelessness. Where an eligible applicant seeks help from the local housing
authority they they are owed the relief duty. The local authorities have to stake steps in order to prevent homelessness, or provide relief duty otherwise.
Steps might include the provision of a rent deposit, debt advice or finding alternative housing arrangements.

The prevention duty lasts for up to 56 days, and is available to all those who are at threat of being homeless.

Those who have a priority need  are provided with interim accommodation whilst the LHA carries out the reasonable steps.

source: [Homelessness Reduction Bill - Fact Sheet](https://assets.publishing.service.gov.uk/media/5a8151bae5274a2e8ab53553/170203_-_Policy_Fact_Sheets_-_Relief.pdf)

One of the key initiatives is procuring affordable houses to those who are at risk.

Below is a chart which show how government spending and house procurements efforts evolved:

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/1a540166-fb6f-4160-8b2a-34378c0c5c14">


As we can see from the chart, the house procurement figures have stagnated around a constant level, as is the same for homeless figures, however relief spending increased.

This suggests that spending on relief has increased for other reasons other than house procurement initiatives and homelessness.

The most likely cause is the rise in the cost of living which we have seen in previous charts.

## **Suggestions based on previous analysis**

Based on what we have seen from the data, we have found disparities in terms of homelessness, and relief spending across regions and age groups.

As we have eliminated economic factors as potential reasons for the disparities, this leads us to deduce that social regional differences and inequality of opportunities between age groups are at play.

Government iniatives should therefore focus on tackling the social inequalities at play.




















