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