# AWS E-commerce Streaming

This project aims at simulating the cloud-based infrastructure of an e-commerce company. 

## Goals

Main goal :
- Process transactions made by customers
- Give customers access to their purchase history

Secondary goals :
- Compute average sales
- Other analytics stats

## Content

- [Dataset](#dataset)
- [Pipelines](#pipelines)
  - [Ingestion](#ingestion)
  - [Stream to S3](#stream-to-s3)
  - [Stream to DynamoDB](#stream-to-dynamodb)

## Dataset

The dataset constisting of 8 columns and 541 909 rows, represents transactions made on the e-commerce website.

Attributes : InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country.

Source : [E-commerce data](https://www.kaggle.com/datasets/carrie1/ecommerce-data) on Kaggle.

## Pipelines

The overall pipeline of the project:<br>
Amazon services used but not indicated on the diagrams are IAM and Cloudwatch. 
![All](diagrams/AWS_ecommerce_streaming-All.png)

### Ingestion

We simulate streaming data by sending each line of a CSV with a Python script to the API gateway.
The lambda function forwards the POST request to a Kinesis Data Stream.
We can then access sent data with a GET request through Postman.
![Ingestion diagram](diagrams/Ingestion.png)

### Stream to S3

Data lake storage

![Stream to S3 diagram](diagrams/Stream_to_S3.png)

### Stream to DynamoDB

![Stream_to_DynamoDB_diagram](diagrams/Stream_to_DynamoDB.png)

