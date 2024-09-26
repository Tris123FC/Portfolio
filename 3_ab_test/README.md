# **A/B Test on Landing Page Conversion Rates**

![image](https://github.com/user-attachments/assets/940b1284-614f-4181-9c8f-6e4057e8723d)

**Motivation:** Conversion rates are crucial for optimizing user engagement and achieving business goals. 
This project involved conducting an A/B test to evaluate whether there was a significant difference in conversion rates between 
two different landing pages. The goal was to determine which page design led to higher user conversions and to provide data-driven 
recommendations for improving page effectiveness.

- **Python File Link:**
  [A/B-Testing](https://github.com/Tris123FC/Portfolio/blob/main/3_ab_test/ab-testing-new-page-conversion.ipynb)

## **The essence of AB Testing**

In its essence, AB testing involves seperating an audience into two equal groups, group A and group B. Each group will experience two different experiences, in our case, two different landing pages.
The researchers who perform the AB test are looking for changes in key performance metrics which suggest preferences from the audience.

<img width="850" alt="image" src="https://github.com/user-attachments/assets/0ec4966c-0448-49b3-91fe-4f8d8d87fb6d">

In the picture above, the audience is looking at two landing pages. Here the key performance metric is conversion rate.
The landing page that group B experienced performed better with a 40% conversion rate. The landing page from group A on the other hand only had a conversion rate of 20%.
Based on these results,a company can assume that the landing page B provides a better experience to users, and they can now optimise their website to improve conversion figures.

From this example, we can clearly see the benefits from AB testing, it is simple to perform and easy to interpret.

## **Using Python Programming to Perform AB Testing**

Performing an AB test using Python is the same as with other statiscal tools, with a little bit more coding.
You have to gather the data, clean it, organise it. Then, you must explore the data to find the key insights it showcases. 
And of course in the end, you have to test for significance, as every sample data is only usefeful if it is representative the general population the sample was taken from.
For this case, I chose to perform Z-test as our data sample is quite large with over 300,000 rows of data.

## **Here is a diagram of the process:**

<img width="850" alt="image" src="https://github.com/user-attachments/assets/b0042085-2b05-4353-a82a-84cbc0d1dbaf">

## To See the AB-Test coding process and analysis, click the link here: [Full Analysis](https://github.com/Tris123FC/Portfolio/blob/main/3_ab_test/ab-testing-new-page-conversion.ipynb)
