# dynamoDB-kafka
  <img src="https://github.com/atifmerghad/atifmerghad/raw/master/Badges/dev/services/aws.svg" alt="AWS" style="vertical-align:top; margin:4px">   <img src="https://github.com/atifmerghad/atifmerghad/raw/master/Badges/dev/tools/bash.svg" alt="Bash" style="vertical-align:top; margin:4px">


This is a demo Lambda function that produces events to a Kafka topic, notifying consumers about new records in DynamoDB.

To deploy this, you'll need:

* Apache Kafka cluster. I used Confluent Cloud, AWS MSK.

* Create a deployment package for lambda - this is a zip that contains the lambda_dynamodb_kafka.py file and all the dependencies. In this case, the dependency is kafka-python, and you can pull it into the zip by running: 
> pip install kafka-python -t

* Upload the package to Lambda. I used the GUI. Make sure the handler is lambda_dynamodb_kafka.lambda_handler, that you set the privileges correctly and that you use Python 2.7.

##Testing

