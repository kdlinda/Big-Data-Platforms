### Create new Hadoop directory
hdfs dfs -mkdir -p /user/hadoop/ex27

### Copy tree text file
hdfs dfs -put ./arbres.csv /user/hadoop/ex27/arbres.csv

### Run program
hadoop jar ex2.7.jar year.height.tree.DisplayCSV /user/hadoop/ex27/arbres.csv /user/hadoop/ex27/ex2.7.txt

### Get output
hdfs dfs -get /user/hadoop/ex27/ex2.7.txt

### Display output
cat ./ex2.7.txt
