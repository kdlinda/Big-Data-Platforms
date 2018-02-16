### Create new Hadoop directory
hdfs dfs -mkdir -p /user/hadoop/ex28

### Copy isd history text file
hdfs dfs -put ./arbres.csv /user/hadoop/ex28/isd-history.txt

### Run program
hadoop jar ex2.8.jar year.height.tree.DisplayFile /user/hadoop/ex28/isd-history.txt /user/hadoop/ex28/isd-output

### Get output
hdfs dfs -get /user/hadoop/ex28/isd-output

### Display output
cat ./isd-output
