# Exploratory Data Analysis

## 1.1 - Data Structure



## 1.2 - Estimates of Location

**Note:** The difference reflects the approach of statistics versus that of data science: accounting for uncertainty lies at the heart of the discipline of statistics, whereas concrete business or organizational objectives are the focus of data science. Hence, statisticians estimate, and data scientists measure. 

## 1.2.1 - Mean (Average) and Variations

- The mean is the sum of all values divided by the number of values.

$$mean = \frac {\sum_{i=1}^n x_{i}}{n}$$

- A variation of the mean is a `trimmed mean`, which you calculate by dropping a fixed number of sorted values at each end and then taking an average of the remaining values.

$$trimmed-mean = \frac{\sum_{i=p+1}^{n-p}x_{i}}{n− 2p}$$

- A trimmed mean eliminates the influence of extreme values.

- A `weighted  mean`  is calculated  by  multiplying  each data  value  $x_{i}$  by  a  user-specified  weight  $w_{i}$  and  dividing  their  sum  by  the  sum  of  the weights.

$$weighted-mean=\frac{\sum_{i=1}^{n}w_{i}x_{i}}{w_{i}}$$

- `Two motivotion for weighted-mean`:
  - Some  values  are  intrinsically  more  variable  than  others,  and  highly  variableobservations are given a lower weight.
  - The  data  collected  does  not  equally  represent  the  different  groups  that  we  areinterested  in  measuring.

## 1.2.2 - Median

- `The median` is the middle number on a sorted list of the data.

- Compared to the `mean`, which uses all observations, the `median` depends onlyon the values in the center of the sorted data.

- The median is referred to as a robust estimate of location since it is not influenced byoutliers (extreme cases) that could skew the results.

- `A  trimmed  mean`  is widely used to avoid the influence of outliers.

### Key ideas

- The  basic  metric  for  location  is  the  mean,  but  it  can  be  sensitive  to  extremevalues (outlier).

- Other metrics (median, trimmed mean) are less sensitive to outliers and unusualdistributions and hence are more robust.

## 1.3 - Estimates of Variability

 `The heart of statistics` lies variability: measuring it, reducing it,distinguishing  random  from  real  variability,  identifying  the  various  sources  of  realvariability, and making decisions in the presence of it.
- `Variability`, also referred to as dispersion, measures whether the data values are tightly clus‐tered or spread out.

**Key Terms :**

| Term          | Definition    | Synonym  |
|:------------- |:-------------|:--------|
| Deviations      | The difference between the observed values and the estimate of location |errors,residual|
| Variance      | residualsVarianceThe sum of squared deviations from the mean divided by n – 1 where n is thenumber of data values| mean-squared-error |
|Standard deviation| The square root of the variance |    -    |
|Mean absolute deviation| The mean of the absolute values of the deviations from the mean|l1-norm, Manhattan-norm|
|Interquartile range|The difference between the 75th percentile and the 25th percentile|IQR|

### 1.3.1 - Deviations

- The `mean absolute deviation` is  to  take  the  average  of  the  absolute  values  of  thedeviations from the mean.

$$mean-absolute-deviation = \frac{\sum_{i=1}^{n}|x_{i}-\bar{x}|}{n}$$

- The  `variance`  is  an  average  of  the  squared deviations.

$$variance = s^2 = \frac{\sum_{i=1}^{n}(x_{i}-\bar{x})^2}{n}$$

- `The standard deviation` is the square root of the variance
$$s = \sqrt{variance}$$

- `The variance`, `the standard deviation`, nor `the mean absolute deviation` is robust to outliers and extreme values.

- A robust estimate of variability is the `median absolute deviation from the median` or MAD.

$$median-absolute-deviation = Median(|x_{1}-m|,|x_{2}-m|...|x_{n}-m|)$$

where `m` is the median.


- the MAD is not influenced by extreme values.

### 1.3.2 - Percentiles

*pass*

## 1.4 - Data Distribution

**Key Terms :**

| Term          | Definition    | Synonym  |
|:------------- |:-------------|:--------|
| Boxplot     | A plot introduced by Tukey as a quick way to visualize the distribution of data. |whiskers plot|
|Frequency table|A tally of the count of numeric data values that fall into a set of intervals (bins).| - |
|Histogram |A  plot  of  the  frequency  table  with  the  bins  on  the  x-axis  and  the  count  (or  pro‐portion) on the y-axis. |- |
|Density plot|A smoothed version of the histogram, often based on a kernel density estimate.|-|

**Key Ideas :**

- A  frequency  histogram  plots  frequency  counts  on  the  y-axis  and  variable  valueson the x-axis; it gives a sense of the distribution of the data at a glance.

- A  frequency  table  is  a  tabular  version  of  the  frequency  counts  found  in  ahistogram.
- A boxplot—with the top and bottom of the box at the 75th and 25th percentiles,respectively—also  gives  a  quick  sense  of  the  distribution  of  the  data;  it  is  oftenused in side-by-side displays to compare distributions.
- A density plot is a smoothed version of a histogram; it requires a function to esti‐mate a plot based on the data (multiple estimates are possible, of course).


## 1.5 Binary and Categorical Data

**Key Terms :**

| Term          | Definition    | Synonym  |
|:------------- |:-------------|:--------|
|Mode |Most commonly occurring category or value in a data set. |-|
|Bar charts|Frequency or proportion for each category plotted as bars.|-|
|Pie charts|The frequency or proportion for each category plotted as wedges in a pie.|-|

**Key Ideas :**

- Categorical data is typically summed up in proportions and can be visualized in a
bar chart.
- Categories might represent distinct things (apples and oranges, male and female),
levels of a factor variable (low, medium, and high), or numeric data that has been
binned.

## 1.6 Correaltaion
