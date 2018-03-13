# Goal:
calculate the PageRank score (with damping factor 0.85) for each user in the Epinions who-trust-whom online social network

# To Run:
## 1. Launch hadoop:

$ start-dfs.sh

## 2. Input directory

$ hdfs dfs -mkdir -p /Q_52/input

## 3. Download necessary files

$ hdfs dfs -copyFromLocal soc-Epinions1.txt /Q_52/input

## 4. Run Hadoop Streaming
$ hadoop jar ./hadoop-streaming-2.6.0-cdh5.12.0.jar \
-input /Q_52/input/soc-Epinions1.txt \
-output /Q_52/output_1 \
-file ./MapperMaster.py \
-mapper MapperMaster.py

declare -i n

n=10

for i in $(seq 1 10);

do
    
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.12.0.jar \
	-input /Q_52/output_$i \
	-output /Q_52/output_$((i+1)) \
	-file ./mapper.py \
	-mapper mapper.py \
	-file ./reducer.py \
	-reducer reducer.py
done

## 5. Get Output

$ hdfs dfs -get /Q_52/output_$((n+1))

$ cat ./Q_52/output_$((n+1)) | python GetOutput.py
