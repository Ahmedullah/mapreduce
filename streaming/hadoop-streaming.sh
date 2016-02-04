#!/usr/bin/env bash

HADOOP_STREAMING_LIB=${HADOOP_INSTALL}/"share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar"

if [[ $# -eq 4 ]]; then
	echo "***** Hadoop Streaming (Hadoop 2.7.1)"
	echo "***** Mapper code location -> "$1
	echo "***** Reducer code location -> "$2
	echo "***** Input file -> "$3

	echo "***** Deleting MR2 output folder -> /"$4
	hdfs dfs -rm -R $4

	hadoop jar $HADOOP_STREAMING_LIB -mapper $1 -reducer $2 -input $3 -output $4
else
	echo "Usage: hadoop-streaming.sh mapper_code reducer_code input_folder output_folder"
fi


