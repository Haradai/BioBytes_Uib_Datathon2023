# Bio datathon UiB 

# Introduction:
we were presented with blbalbla

# Initial exploration:
Correlation plots etcc

# What we want to answer
The instructions were pretty open regarding what we could do with the data. For us, it was interesting to find out how the **different treatments** impact the life thats in it, regarding the **concentrations of dna** found.

Initially, we thought about it broadly, hence we asked ourselves:
## **How is the biodiversity impacted by treatment?**

First we had to define a measure of diversity.

Thanks to chatGPTs recomendation we found the **Shannon-Wiener Diversity Index (H').** Which is a measure used to measure the diversity of species in a community.

This is defined by the equation **H = -Σpi * ln(pi)** where pi is the proportion of each individual in the community.

This is what we found:

<img title="a title" alt="Alt text" src="imgs/diversity_plot.png">

***[some conclusions!!!]***

## **How do the different treatments impact the populations?**

Again, looking at the dna percentage **by specie** in the samples we attempted to discover if:

 1. Treatments overall affect species population
 2. What treatments affect the most

As a simple measure of what each population was doing in each sample we applied linear regression to output a slope, which would serve as an indicator of growth/decrease and its speed.
Our dataset looked like this:
 
<img title="a title" alt="Alt text" src="imgs/species_df.png ">


***[1.]** Do treatments overall affect species population?*

In order to determine **how much were the treatments relevant in the changes of population trend(slope)** we performed an **ANOVA analysis**. This way we can get a statistical significance "confidence" value regarding if a concrete specie is affected by the treatments.

Before starting though, we had to make sure the following, as this is some **assumptions** this method makes on the data. It is essential in order to be able to **consider the results valid.**

*1. The observations are independent within and among groups.
2. The observations within each group are normally distributed.
3. The distributions from which the samples are drawn have the same finite variance.*

**What can we say about our data?**
*1. -> We have replicas, so therefore not really. We should only grab one replica of each.
2. -> We will assume this is true, that the dna is homogeniouslly distributed in the sample medium.
3. -> Again, as in 2 we will assume homogeneous medium.*

After removing replicas, this is the result we got for the ***Homo Sapiens Specie*.**
**p_value = 0.0011488636867922114**

Typically in ANOVA analysis a p_value of **0.05 is the threshold** to determine if there is a **statistical significance** or not. In this case it is **below, so we have some!**
Note: we utilized the function *f_oneway* from the *scipy statistics* package.

After this result, we continued to determine, **how does this affect all other species?** Hence, we did the exact same calculation for all 


<img title="a title" alt="Alt text" src="imgs/pvalue_all_species.png">

**What percent of species are significantly affected by the treatments?** --> 4.35%


---

**ML approach to steer formulating an hypothesis**: 
If we attempt to classify...


HENRIK PART


+DL part??? (TODO)


## **How does treatment affect water conditions?**
In order to answer this question we attempted to create some simple ML classifiers, SVM and KNN. They attempted to classify the applied treatment by using the water conditions as features. 
The idea is that if we are able to make a model with a decent accuracy that **could** mean that there is some relation between  them.

**Results:**
We didn't manage to classify. We cannot conclude from this that the inability to classify means that there is no relation so we could consider it non conclusive. Anyhow, talking to *Natacha* she mentioned that the scientists taking the samples were trying to make the conditions stable, which aligns with having no relation between them.

## What conditions are related to the increase or decrease of certain species?

