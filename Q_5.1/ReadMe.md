# Goal: calculate Term Frequency-Inverse Document Frequency (TF-IDF) of a set of documents using MapReduce. In particular, you will use the following documents that you will add to HDFS

# Example:
hadoop fs -mkdir input
 wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
hadoop fs -copyFromLocal defoe-robinson-103.txt input
wget http://www.textfiles.com/etext/FICTION/callwild
hadoop fs -copyFromLocal callwild input

# To Run:
1. Launch hadoop
2. Run the .sh file to obtain outputs
