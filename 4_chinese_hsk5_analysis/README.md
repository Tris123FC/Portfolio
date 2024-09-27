# Analysis of Chinese Vocabulary in the HSK5 Textbook

## Motivation:
Understanding and mastering the vocabulary for the HSK5 (Hànyǔ Shuǐpíng Kǎoshì Level 5) Chinese proficiency exam is crucial for learners aiming to reach advanced language skills. This analysis involved examining the target vocabulary of the HSK5 level and assessing their frequency in both intermediate and advanced texts. By analyzing the occurrence of these words in different levels of difficulty, the project aimed to uncover trends in vocabulary usage, determine which words are most critical for achieving fluency, and provide insights for more effective language learning strategies. The goal was to guide learners and educators in optimizing study plans and ensuring better preparation for real-world language use.

**Data Source:**

[Tableau - Chinese Character Analysis](https://public.tableau.com/app/profile/tristan.cross/viz/AnAnalysisofHSK5CharacterFrequencyinIntermediatetoAdvancedText/Dashboard1#1)

[Scrapped Website - Level Reading Webpage](https://hskreading.com)

[HSK5 - Vocabulary List](https://mandarinbean.com/new-hsk-5-word-list/)



## Project Snapshot
![Project Screenshot](images/dashboard.png)

## Topic Introduction

Language learning is a passion of mine as it is for many other. There is nothing more satisfying than reaching a level where you are able to communicate with native speakers, and this is true for every language, as you suddenly feel engrossed in the culture surrounding the language. This reminds of a time when I was in the back of a Chinese taxi, and the driver started to ask me all of these questions. Chinese taxi drivers are notoriously known for their excessive friendly nature: if you are able to say "Hello" in Chinese, they will praise you for your authentic level of Chinese so you often just nod and smile as they keep talking to you , but after 3 years of studying Chinese intensely, when the driver started talking to me, and I was able to respond back, that was probably one of my proudest moments. Unfortunately, to get to this level, a great amount of studying is needed, and the most annoying part of learning a language, is studying the textbook.

## The Textbook

The main textbook for studying chinese language is titled HSK (Hànyǔ Shuǐpíng Kǎoshì) or in English, Chinese Level Test. It comes in six installements, from HSK1 to HSK6. 

Below is a break down of the vocabulary count according to each installement:

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/a80514e2-5bbf-402a-9242-adfa69af28bd">

Books increase in difficulty, only requiring learners to study 150 characters at first, gradually increasing in difficulty until they are familiar with 2500 characters. I currently finished reading the HSK5 book, so I am supposed to know 2500 words (supposed...). The problem is that I don't, and it is because most of the time you don't use the textbook vocabulary in your conversation, or even in writing. But even though these vocabulary words aren't often seen in practice, they are essential building blocks, providing you with the foundations to study the vocabulary that you want to use to communicate with friends or business partners.

This is the reason for my analysis: I want to decypher the new word vocabulary in the HSK5 books to find trends and patterns which might assist learners who are also at the textbook stage.

## Analysis Process

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/8701a370-51c1-4f3f-b472-53bd128d6fcc">


**Step 1:** Identifying the Data Source:

We need a reference for the HSK5 vocabulary list and a source of texts for Chinese learners seperated by proficiency level.
The reference for the HSK5 vocabulary list was easy to find, and can be asscessed from [mandarinbean.com](https://mandarinbean.com/new-hsk-5-word-list/).

After researching and comparing websites, I assessed the best website for data collection was [hskreading.com](https://hskreading.com). The chosen website possessed over 100 texts seperated by levels from beginner, to advanced.

**Step 2: Gathering the data:**

Due to the quantity of texts and the amount of characters involved. The only way to gather the data was using programming. I created a simple scraping tools which was able to open the the sections of the website which we are interested, go through the list of texts and copy the them into a word document. This process was not ideal as the Word software would struggle with the amount of chinese text characters copied into the file, however after succesfully copying all of the texts from the website to the word file, I did not need to open the files through the software as I could access it through a simple python program. I was able to count all of the characters in the Word document that are in the HSK5 reference list and input the data into a Excel table. The result is a list of HSk5 vocabulary list which a count of their occurences in intermediate and advanced text.

**Step 3: Checking the output data:**

After running the program to count the occurences of vocabulary words, quikly comparing the data in the Excel and Word documents proved that the data was valid and reliable. Looking at the quantity of characters in the text we gathered, I decided that the amount of data was sufficient for a basic analysis of character occurences in texts (analysed nearly 80 text with approximately 6000 characters).

**Step 4: Reading the data:**

We have gathered the data and organised it into table format. Now comes the fun part, visualising and intepreting data.
For this analysis I chose to use Tableau public as it provides an intuitive platform for designing charts eye-catching charts with interactive elements.

## Exploring Data Through Visualisation

**Analysing Word Frequency in Text** 

Below is a bubble park chart provides a quick glimpse at the most occuring HSK5 characters in intermediate to advanced text.

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/a782ec0c-b0bb-4fad-9caf-1f1651a7531d">

By hovering the mouse over the circles in the chart, we can see the Chinese character, it's phonetic sound, the English translation and the number of occurences found.
Beside the chart is a small table which provides summary statistics on the scale of our analysis.

One thing to notice is that of the 1000 characters we researched in our HSK5 list, maybe only 10% of the characters.

Below is a table that checks the of instances where a character got 0 occurences, 1  occurence, 2 occurences and so on:

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/acc1418a-be8f-4aef-aafd-059abf6931ae">


We can see that of that 70% of the words in our HSK5 list had 0 occurences in nearly 80 texts, 13% of words had only 1 occurence, and as we go on and on, the probability of words having more than 5 occurences becomes less than 1%.

This is no surprise, as we think about English and all of the words they we do not use, the same is true for Chinese and maybe more so because of the vast amount of characters in its language. According to the CLI institution for Chinese language, there are well over 100,000 different characters, with 2,500 characters commonly used. Quick question to the reader: how many English words do you estimate you use everyday?

**Comparing Intermediate and Advanced Texts**

How do word occurences change as we progress through levels of difficulties?

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/aa714a54-6d86-4a87-8040-253c05a7469c">

From the bar chart, we can see osberve there is an inverse relationship between levels. As we switch from intermediate to advanced texts, the frequency of these Chinese characters decreases or increases depending on their complexity. This can be seen a natural phenomenon of language progression, as we grow older, we remove the simple words we use as a child from our lingo and add more sophisticated words to try and impress our friends (it doesn't matter if we understand the meaning or not. As we progress through the level, we stop using the basic vocabulary we learning in the previous texts and start using more complicated words.

**Summary of our finding:**

- The data was able to offer us quick insight on the most occuring words in intermediate and advanced texts. The table can provide guidance on phonetic pronunciation and English meaning.

- Over 70% of the vocabulary list never occured in the nearly 80 texts which we analysed. This trend can be seen as normal languages hold a huge number of words which people rarely use.

- There is an inverse relationship between levels of difficulty and word occurence. As people get more adept at their language, they use more complex words over the language that they used previously.











