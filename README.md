# ADBC Writing to PostgreSQL Database
In this repository, we introduce an experiment that shows how much Arrow Database Connectivity (ADBC) is efficient in writing big datasets to PostgreSQL database. The experiment is conducted on a dataset of 10 and 40 million rows and 3 columns. The dataset is generated randomly using Python's pandas library. I use Jupyter Notebook to run the experiment.    

## What is [ADBC](https://arrow.apache.org/adbc/current/index.html)?  
It is an API collection that allows Arrow-native to access databases. It executes SQL queries, database catalogs, and more. It leverages Apache Arrow to avoid making copies of data on reads and speed up data access with eliminating serialization overhead. In addition, the driver is responsible for converting objects from/to arrow where required and that helps developers focus on their main objective.  

## Experiment
We compare the performance of ADBC driver and SQLAlchemy which is a popular Python SQL toolkit and Object-Relational Mapping (ORM) library. We measure the time taken to write 10 and 40 million rows to a PostgreSQL database. The experiment is conducted on a local machine with 16GB RAM and 8 cores.

To replicate the experiment, please follow this short artice that explains the code, the installation process and the experiment.  
<!-- <a target="_blank" href="https://github-readme-medium-recent-article.vercel.app/medium/@ali.massoud136/e5458c188990"><img src="https://github-readme-medium-recent-article.vercel.app/medium/@ali.massoud136/e5458c188990" alt="Recent Article 0">  -->


## Results
The results show that ADBC is faster than SQLAlchemy in writing big datasets to PostgreSQL database. The time taken to write <u>10 million rows insertion</u> is ***32.4 seconds*** with ADBC and ***1 minute 4.6* seconds** with SQLAlchemy. The time taken to write <u>40 million rows insertion</u> is ***1 minute 33 seconds*** with ADBC and ***4 minutes 30 seconds*** with SQLAlchemy. The results show that ADBC is 2.3 times faster than SQLAlchemy in writing 10 million rows and 2.2 times faster in writing 40 million rows.

