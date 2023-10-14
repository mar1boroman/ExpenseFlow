# Redis Vector Search to Categorize Financial Transactions

<div align="center">
    <a href="https://github.com/mar1boroman"><img src="assets/redis-favicon-144x144.png" width="30%"><img></a>
    <br />
    <br />
<div display="inline-block">
    <a href="https://redis.io/docs/stack/search/reference/vectors/"><b>Redis VSS Documentation</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://www.redisvl.com/docs/html/index.html"><b>Redis VL Documentation</b></a>&nbsp;&nbsp;&nbsp;
  </div>
    <br />
    <br />
</div>

# About this demo application

With this demo application, we use a pre-labelled set of transactions [train.csv](data/train.csv) to predict the categories of a seperate transaction log [test.csv](sample/test.csv).
This usecase is specially useful if your fintech application needs to build a expense tracker or categorizer.
This approach also avoids the task of finetuning the AI models and allows you to use off the shelf pre-trained model.
This demo uses the Open AI text embedding model, you need a functioning Open AI API key to test this application


In this particular demo application, we use the library [redisvl](https://www.redisvl.com/docs/html/index.html) which is a python library helping you to use the redis vector database functionality in a hassle free manner.

## Project Setup

### Spin up a Redis instance enabled with RedisStack!

The easiest way to is to use a docker image using the below command
```bash
docker run -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

If you do not want to use a docker image, you can sign up for a free Redis Cloud subscription [here](https://redis.com/try-free).

###  Set up the project

Download the repository

```
git clone https://github.com/mar1boroman/ExpenseFlow.git && cd ExpenseFlow
```

Prepare and activate the virtual environment

```
python3 -m venv venv && source venv/bin/activate
```

Install necessary libraries and dependencies

```
pip install -r requirements.txt
```

**Configure your OPEN AI Key in the .env file**

```
vi .env
```

### Using the project

```
streamlit run ui/0_📎_Upload_Pre_Labelled_Data.py
```

In the first screen upload the [train.csv](data/train.csv) file to load the embeddings of pre-labelled data

In the 🔮_Predict_Categories screen load the [test.csv](sample/test.csv) file to predict the category of every transaction and show an aggregated view of the expense

If you want to check a sample step by step exection (behind the scenes view), the third screen allows you to enter a single transaction description manually and see how the category of the transaction is predicted.