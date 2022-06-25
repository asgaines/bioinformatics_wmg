# Bioinformatics

## q1

Parse through FASTA-like file and find missing number in sequence of length determined by annotation integer.

### Build

```
cd q1
docker build -t wmgq1 .
```

### Run

```
docker run -it --rm --name wmgq1_run wmgq1 $ARG
```

Where `$ARG` is a positional argument for the file path to a target sample text file. A number of sample files are provided. For example:


```
docker run -it --rm --name wmgq1_run wmgq1 ./flatfiles/question_one.txt
```

### Tests

To run test suite:

```
docker run -it --rm --name wmgq1_run --entrypoint=python3 wmgq1 -m unittest
```

## q2

Annotate mass spectrometry data, finding metabolites and adducts that minimize the noise from a signal reading.

### Build

```
cd q2
docker build -t wmgq2 .
```

### Run

```
docker run -it --rm --name wmgq2_run -v ${PWD}:/usr/src/app wmgq2 flatfiles/toy.txt results.txt
```

Results of the run are written to the last argument provided (`results.txt`). A number of sample files are provided. For example:


```
docker run -it --rm --name wmgq2_run -v ${PWD}:/usr/src/app wmgq2 flatfiles/2.txt results.txt
```

### Tests

To run test suite:

```
docker run -it --rm --name wmgq2_run --entrypoint=python3 wmgq2 -m unittest
```