# Goal:
calculate Term Frequency-Inverse Document Frequency (TF-IDF) of a set of documents using MapReduce

# To Run:
## 1. Launch hadoop:

    $ start-dfs.sh

## 2. Input directory

    $ hdfs dfs -mkdir -p /Q_51/input

## 3. Download necessary files

    wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
    $ hdfs dfs -copyFromLocal defoe-robinson-103.txt /Q_51/input

    wget http://www.textfiles.com/etext/FICTION/callwild
    $ hdfs dfs -copyFromLocal callwild /Q_51/input

## 4. Run Hadoop Streaming

    $ hadoop jar ../hadoop-streaming-2.6.0-cdh5.12.0.jar \
    -input /Q_51/input \
    -output /Q_51/output \
    -file ./mapper.py \
    -mapper mapper.py \
    -file ./reducer.py \
    -reducer reducer.py

## 5. Get Output

    $ hdfs dfs -get /Q_51/output/part-00000

# Output:
Please see the solution for the exercise under the document part-00000 in the output folder.
