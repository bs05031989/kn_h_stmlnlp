"""
Statistics : There are primarily two types of statistics

1. Descriptive 
2. Inferential

Some Main Descriptive Statistics Topics :
a) Summarizing Data Sets (Mean, Median, Mode, Range, Quartiles, etc.)
Measure of central tendency
b) Measure of Dispersion (Standard Deviation, variance)
c) Histogram,Pdf,Cdf,Univariate Analysis, Bivariate Analysis
, Correlation Coefficient, Covariance Matrix, Box Plot.

Some main Inferential Statistics Topics :
A) Null Hypothesis, Alternate Hypothesis
, Type I and II Errors (Probability of type I error = alpha , Probability of type II error = beta)
Ztest,T-test,Chi-square Test,ANOVA
Sample data ---------- Population.
Data : Statstools
DATA NEVER LIES : POWERBI, Tableau : KPI Analysis

Statistics : It is a science of collecting, organizing and analyzing datasets.
Data : Facts, Piece if information.

Examples : Heights of students in class [150,160,170]

Descriptive Statistics : It consists of organizing, & summarizing of data

Measure of central tendency : Mean, Median,mode

Measure of Dispersion : Standard Deviation, variance

Histogram,Pdf,Cdf,Univariate Analysis, Bivariate Analysis

Different types of distribution of data


## Inferential Statistics : It contains the statistical methods that are used to draw conclusions from a sample.

From Sample to Population

Example : 10 People in a class | Age collected 

1. Descriptive Use case : What is the common age of the class| Mean, Median, Mode.
2. Inferential Statistics use case: How does this mean affect the population? | t-test, ANOVA etc.. Does this 
sample mean shows the real population of university ages as well.

Sampling Techniques

# Population : Area of intrest for study.
# Sample : A small fraction of population represnting the whole Example : Exit Poll

Goal of sampling is to create a sample that is reprsentative of the entire population.
Population (N)  | Sample (n)


Types of Sampling :
1. Simple random sampling : Every member of the Population have equal chance of being selected for the sample(n).

2. Startaified Sampling : Layered non overlapping Ex : Gender M|F

3. Systematic Sampling : Ex : Mall outside , Every 4th Person Survey.

4. Convinience Sampling | Voluntary response sampling : Domain Specific Expertise needed : Survey Domain specific.

Example 1. Exit Poll : Random Sampling 2. Doctor Survey : Convienience 3. Height Measurement Gender Based : Stratified.

## Variables : It is a property that can take on many values.
Ex : Height [171,172.5]  Weight [45,67]

Until not specifically mentioned Variables works in a single mode

Plural Mode [23,34,56] | Weight |List


Types of variables :

1. Quantitative 2. Qualtitative

1 Quantitative : a) Discrete b) Continious

a) Discrete : It should be a whole number (No of bank account : like 3 )
b) Continious : Need not to be whole number (Height [123,125])

2. Qualtitative : It seems like categoriacal : Classification

Types of Flowers : Lily,Rose,Almond 
Classification based on some properties.

Measure of central tendency

1 Mean 2) Median 3) Mode 

It is used to measure the central distance 

Mean : Average , It is not good in case of outliers

Median : First sort all the numbers
 Two cases : if set is odd : Its easy to locate [1,2,3,4,5] Median =3
            If setis even : [1,2,3,4,5,6] Median  Take average of 3 & 4 Median 3.5

            It helps us to avoid outliers

Mode : It is useful in the categorical elements.

It considers the most frqusent element in the set.

[1,2,3,4,4,4,5,5,5,5,7,7,7,7,,777,]  Mode =7

### Measure of Dispersion :

Standard Deviation : It is used to measure the dispersion in a set.
Variance : It is used to measure the dispersion in a set. 

1. First we need to calculate X bar : Sample Mean
2. Then we need to calculate Sample variance  (xi-xbar)^2/(n-1)

Variance : It is a measure of how far a set of numbers are spread out from their average value.

3. Standard Deviation = Square root of Variance

SD : It tells us about the spread of the data.


## Percentile/Quartile

Percentage : [1,2,3,4,5] : Ex : Percentage of even numbers in the set : 2/5 40 Perecent

Percentile : It is a value below which a certain percentage of observation lies

Ex : 95 Percentile : Person got better marks than 95 percent of the entire students.

Ex : [2,2,3,4,5,5,5,6,7,8,8,8,8,9,10,11,12]
 
 What is the percentile rank of 10
 n = 17
 Number of value below (10/n)X100
 (15/17)x100 =88.23

 What value exists at percentile of 25.

 Value index : (Percentile/100)x(n+1)
 Value Index : 4.5
Average of 4&5 : 5

### Quartile : 1/4th
1st Quartile : 25% : Q1
3rd Quartile : 75% : Q3

Inter Quartile Range : IQR Q3-Q1

Five Number Summary
1. MIn 
2. Q1 : First Quartile : 25%
3. Median 
4. Q3 : Third Quartile : 75%
5. Max : Anamoly cant be considered as max 

How to find the Anamoly in a set [1,2,3,4,5,6,7,8,9,234]

Find a Lower fence and Higher fence.

1. Find first the Q1 & Q3
Quartile = (Percentile/100)x(n+1) : It will give the index value 

2. Lower fence = Q1-1.5(IQR)  | IQR =(Q3-Q1)
3. Higher Fence =Q3+1.5(IQR)

###  Normal Gaussian Distribution

a) It is symmetrical. Starts from mean (mu + sigma )
b) It follows the principle of 68-95-99

Example : Height of a sample population, Weight of a sample population

# Central Limit Theorem 

From the given population: if we take sample having n>30 , multiple samples and take their mean, it is always going to behave like normal distribution.

# Log Normal Distribution 

if X = Log Normal Dist
then y =ln(X)  : Normal Distribution

Example : Wealth Distribution

# Power Law (Pareto Distribution) (alpha = Hyperparameter)

1) It works on the 80-20 Principle

Ex : 80% of the population has 20% of the wealth.
Pareto Distribution can also be transformed to Normal Distribution  using Box-cox transformation.





















"""