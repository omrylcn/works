# Core Concepts

## Load Leveling with Queues

- Messaging queues can be used between the data producers and data consumers in a bigdata system, for load leveling.

- Queues are are useful for push-pull messaging where theproducers push data to the queues and the consumers pull the data from the queues.

- It is using to prevent the consumers from being overloaded during peak loads.

- The producers and consumers do not need to be aware of each other and can run asynchronously.

- When queues are used, the consumers can be scaled-up or down based on the load levels. 

- Queues help in improving the system reliability and availability.

## Load Balancing with Multiple Consumers

- Having multiple consumers can help in load balancing and making the system more scalable,reliable and available.

- Multiple consumers can make the system more robust asthere is no single point of failure.

- Load balancing between consumers improves the system performance as multipleconsumers can process messages in parallel.

- This patterns is useful when the messages canbe processed independently without any dependencies.

- When a consumerretrieves a message, it is not deleted from the queue, but hidden from other consumers (with a visibility timeout) to prevent duplicate processing.  After the message is processed, the consumer deletes it from the queue. In case the consumer fails while processing a message,the message become available to other consumers after the visibility timeout period. This ensures that the message is not lost and is processed by one of the consumers before being deleted.

## Leader Election

- There is a need for coordinating the actions performed by the instances, as the instances may be accessing shared resources. 

- Coordination becomes important when the instances are running in parallel and each instance is computing a small portion of acomplex computation.

- In such distributed systems, a leader is assigned the role of managingthe instances and coordinating their state and actions.

- In the simplest leader election mechanism the instancewith the highest ID is elected as the leader.

- When the leader election process is run, the instances communicate amongst themselves and elect the instance with highest ID as their leader.Each instance is aware of the leader when the election process is completed.

- An important requirement for any leader election mechanism is that the mechanism should be able to elect exactly one instance as the leader and all the instances should know who the leader is when the election process completes.

- Another leader election algorithm is the `Bully algorithm` (more information : <https://www.youtube.com/watch?v=z6PQGVcKXrk&ab_channel=Education4u>  or <https://www.cs.colostate.edu/~cs551/CourseNotes/Synchronization/BullyExample.html>).

## Sharding

- Sharding involves horizontally partitioning the data across multiple storage nodes in a datastorage system.

- When applications have large number of concurrent users, sharding can helpin improving the system performance and response times for the users as the queries areserved by multiple nodes.

- Sharding enables thestorage system to be scaled out by addition of new nodes.

- The data shards (partitions) can be replicated across the storage nodes to make the system more reliable. When the shards are replicated, load balancing of queries can be done to improve the response times.

- Sharding strategies determine which datashould be sent to which shard. Most sharding strategies use one or more fields in the data as the shard key (or partition key) (DynamoDB).

- The most common approach is to use a hash function that evenly partitions the data across the storage nodes.The hash function is applied to the shardkey to determine the shard in which the data should be stored.

![shard hash](https://docs.mongodb.com/manual/_images/sharded-cluster-hashed-distribution.bakedsvg.svg)

- The hashing approach prevents a single storage node becoming a hotspot.

- Another approach is to store data within a range of shard keys in one shard. Thesystem maintains a map of the range keys and the corresponding shards.

![shard key](https://docs.mongodb.com/manual/_images/sharded-cluster-ranged-distribution-good.bakedsvg.svg)

- This strategy isuseful when you want to keep data which is retrieved and updated together in one shardto avoid repeated lookups.

- **More resources**:
  - <https://www.digitalocean.com/community/tutorials/understanding-database-sharding>
  - <https://docs.mongodb.com/manual/sharding/>

##  Consistency, Availability & Partition Tolerance (CAP)