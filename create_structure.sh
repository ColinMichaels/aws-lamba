#!/bin/bash

# Define the root directory
ROOT_DIR="lambda_function"

# Create the main directory
mkdir $ROOT_DIR
cd $ROOT_DIR

# Create main.py in the root
touch main.py

# Create utils directory and its files
mkdir utils
cd utils
touch __init__.py logging.py pagination.py credentials.py
cd ..

# Create validation directory and its files
mkdir validation
cd validation
touch __init__.py params.py table_schema.py
cd ..

# Create athena directory and its files
mkdir athena
cd athena
touch __init__.py interaction.py metadata.py cost_estimation.py async_queries.py
cd ..

# Create security directory and its files
mkdir security
cd security
touch __init__.py sanitizer.py
cd ..

# Create s3 directory and its files
mkdir s3
cd s3
touch __init__.py interaction.py
cd ..

# Create query directory and its files
mkdir query
cd query
touch __init__.py builder.py history.py
cd ..

# Create response directory and its files
mkdir response
cd response
touch __init__.py formatter.py
cd ..

echo "Directory structure created successfully!"
