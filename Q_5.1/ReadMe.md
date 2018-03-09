# Goal: calculate Term Frequency-Inverse Document Frequency (TF-IDF) of a set of documents using MapReduce

# To Run:
1. Launch hadoop: 

$ start-dfs.sh

2. Input directory

hdfs dfs -mkdir -p /q51/input

3. Download necessary files 

wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt

hdfs dfs -copyFromLocal defoe-robinson-103.txt /q51/input

wget http://www.textfiles.com/etext/FICTION/callwild

hdfs dfs -copyFromLocal callwild /q51/input

4. Run Hadoop Streaming
hadoop jar ../hadoop-streaming-2.6.0-cdh5.12.0.jar \
-input /q51/input \
-output /q51/output \
-file ./mapper.py \
-mapper mapper.py \
-file ./reducer.py \
-reducer reducer.py

5. Get Output

hdfs dfs -get /q51

cat ./q51/out_round3/part-00000 | python top_20_tfidf.py
