# Apache Spark

## Apache Spark

- `Apache Spark` is a unified engine designed for large-scale distributed data processing,on premises in data centers or in the cloud.

- Spark  provides  `in-memory  storage`  for  intermediate  computations,  making  it  muchfaster  than  Hadoop  MapReduce. 

- Spark’s design philosophy centers around four key characteristics:
  - **Speed** : Spark  builds  its  query  computations  as  a  directed  acyclic  graph  (DAG);  its DAG scheduler and query optimizer construct an efficient computational graph thatcan usually be decomposed into tasks that are executed in parallel across workers onthe cluster.
  - **Ease of use** : Data structure abstractions like RDD,DataFrames and Datasets.
  - **Modularity** : There are many languages API like python,scala,r and many components like Spark SQL,Spark MLlib.
  - **Extensibility**: Spark is used to read data stored in myriad sources - Apache Hadoop, Apache Cassandra, Apache HBase, MongoDB, Apache Hive, RDBMSs - and process it all in memory. It can also be extended to read data from other sources, such as Apache Kafka,Kinesis, Azure Storage, and Amazon S3.

- **Spark Open Sources**

![spark_eco_system](https://databricks.com/wp-content/uploads/2019/02/largest-open-source-apache-spark.png)


- **Spark Stack**

![spark_core](https://bigdatahadoop28feb.files.wordpress.com/2016/11/real-time-analytics-with-apache-kafka-and-apache-spark-19-638.jpg)

- Spark is a `distributed data processingengine` with its components working collaboratively on a cluster of machines.


- **Spark Architecture**

![spark_arc](https://docs.microsoft.com/tr-tr/dotnet/spark/media/spark-architecture.png)


- **Spark driver**:
  - Responsible for instantiating a `SparkSession`
  - Communicates with the cluster manage
  - Requests resources  (CPU,  memory,  etc.) from the cluster manager for Spark’s executors(JVMs)
  - Transforms all the Spark operations into DAG computations,schedules them.
  - Distributes  their  execution  as  tasks  across  the  Spark  executors.
  - Communicates directly with the executors.

- **SparkSession**
  - SparkSession became a unified conduit to all Spark operations and data. 
  - Subsume previous entry points to Spark like the `SparkContext`,`SQLContext`,`HiveContext`,`SparkConf`,  and `StreamingContext`.
  - *More information* : <https://databricks.com/blog/2016/08/15/how-to-use-sparksession-in-apache-spark-2-0.html>

- **Cluster manager**:
  - Responsible  for  managing  and  allocating  resources  for  the cluster  of  nodes  on  which  your  Spark  application  runs.

  
- **Spark executor**:
  - Runs on each worker node in the cluster. 
  - Communicate with the driver program and are responsible for executing tasks on the workers.
  - Only a single executor runs per node in most deployment modes.




## References

- Learning SparkLightning-Fast Data AnalyticsSECOND EDITIONBostonFarnhamSebastopolTokyoBeijingBostonFarnhamSebastopolTokyoBeijing
