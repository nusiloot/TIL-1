# day2 20200507 Spark

## 환경설치

1. Linux 가상머신 m1, m2를 기동한다.

2. Hadoop의 환경 설정을 변경

   - slaves 파일 편집(데이터노드 정보)

     ```
     cd $HADOOP_HOME/etc/hadoop
     ```

     ```
     vi slaves
     ```

     들어가서 slave1만 남기고 저장

   - hdfs-site.xml 파일 편집(복제 개수 설정) -> 1로 변경

     ```
     <property>
           <name>dfs.replication</name>
           <value>1</value>
        </property>
     ```

   - slave1에서 가서도 똑같은 설정을 해준다.

   - `start-dfs.sh` master에서 실행

   - `jps` 명령어 사용해서 확인

     - master에서 
     - slave에서 

   - `hdfs dfs -ls /edudata` 확인!!

### vi  edirot  command 

`:set number` 라고하면 임시로 line number 보여줌\



------

## Apache Spark

아파치 스파크(Apache Spark)는 오픈 소스 클러스터 컴퓨팅 프레임워크이다. 캘리포니아 대학교 버클리의 AMPLab에서 개발된 스파크의 코드베이스는 나중에 아파치 소프트웨어 재단에 기부되었으며 그 이후로도 계속 유지 보수를 해오고 있다. 기존엔 batch processing을 하기 위해 MapReduce를 사용하고, sql을 사용하기 위해서는 hive를 사용하는 등 다양한 플랫폼을 도입해야 했었다.
이제는 Spark 하나만을 설치해도 batch, streaming, graph processing, sql 등의 처리가 가능하다. 또한 Spark은 Java, Scala, Python, SQL, 그리고 R언어의 API를 제공하기 때문에 언어적인 선택의 폭이 넓다.

[ Spark의 특징 ]

- High-Level Tools

- Spark SQL for SQL
  Hadoop의 Hive가 아닌 Spark SQL을 통해 SQL을 MapReduce없이 빠르게 처리가 가능하다.

- 구조적 데이터 프로세싱

  Json, Parquet(파켓 : Apache Parquet은 Apache Hadoop 에코 시스템의 무료 오픈 소스 열
  기반 데이터 저장 형식), DataFrame, DataSet

- MLlib for machine learning
Classification, Regression, Abnormal Detection, Clustering 등의 다양한 machine learning algorithm을 제공한다.

- GraphX for graph processing
  graph processing을 지원하는 GraphX를 제공한다.

- Spark Streaming.
  batch processing 외에도 streaming처리가 가능하다.

- Launching on a Cluster
Sparks를 클러스터에서 동작하게 하기 위해서는 cluster manager가 필요하다.

## Speed

**Run workloads 100x faster.**

Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.

URL 참고: http://spark.apache.org/downloads.html

![image-20200507141738130](C:\Users\seouz\AppData\Roaming\Typora\typora-user-images\image-20200507141738130.png)

```
Download Apache Spark™
1. Choose a Spark release: 
2. Choose a package type:
Download Spark: spark-3.0.0-preview2-bin-hadoop2.7.tgz
```



[spark-3.0.0-preview2-bin-hadoop2.7.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop2.7.tgz) -> 클릭!!!!!!!!!!

[ Spark 설치 방법 ]

1. 스파크 사이트에서 spark-2.4.5-bin-hadoo p2.7.tgz 을 다운로드하고 C:\ 에 압축 해제
2. 다음 환경 변수들을 시스템 변수에 추가한다
   SPARK_HOME      c: spark-2.4.5-bin-hadoop2.7
   PATH                      SPARK_HOME bin SPARK_HOME s bin
   - cmd창에서 
   - echo %SPARK_HOME% --> 확인
   - echo %PATH% --> 확인

3. SPARK_HOME 의 conf 디렉토리로 이동하여 log4j 의 설정파일을 만들 고
   (log4j.properties.template 파일을 log4j.properties로 복사) 로그레벨을 INFO 에서
   WARN으로 변경한다

   **Spark은 가급적이면 in-memory!! 에 올려놓고 한다.**

   1~6단계까지 데이터 전처리를 한다고 하면 모든 전처리 과정을 Conversion(변환)하여 최종적으로 Action을 해야 일을 한다.

```
Transformation -> Transformation -> Transformation  -> Transformation  -> Transformation -> Transformation -> Action
```

- 변환 작업의 명령을 내리면 보관만하다가 수행을 안한다!! -> 그리고 최종적으로 Action을 요구하면 한번에 수행한다!!! -> 좀더 효율적인 작업을 하기 위해 !!

  이렇게 보관만하는 것은 Lineage라고 한다.

  만약 이렇게 일하다가 3단계에서 문제가 생기면 이전 단계로 되돌아가서 다시 실행한다. -> 다시한번 수행을 한다.!! (이 단계는 Lineage에 보관하고 있다.)

4. spark-shell을 실행시킨다.
   [ 워드 카운트 수행 : Scala (인터랙티브 방식) ]