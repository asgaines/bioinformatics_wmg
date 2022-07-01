echo "Beginning pipeline"

echo "Indexing reference genome"
bowtie2-build ngsdata/toy_genome.fa out/toy_genome_index

echo "Aligning baseline reads"
bowtie2 --very-fast-local -x out/toy_genome_index -1 ngsdata/baseline_reads_R1.fastq.gz -2 ngsdata/baseline_reads_R2.fastq.gz -S out/baseline_reads.sam
echo "Aligning copy number variant reads"
bowtie2 --very-fast-local -x out/toy_genome_index -1 ngsdata/reads_R1.fastq.gz -2 ngsdata/reads_R2.fastq.gz -S out/variant_reads.sam

echo "Converting baseline SAM > BAM"
samtools view -b out/baseline_reads.sam > out/baseline_reads.bam
echo "Converting variant SAM > BAM"
samtools view -b out/variant_reads.sam > out/variant_reads.bam

echo "Sorting baseline bam file"
samtools sort out/baseline_reads.bam > out/baseline_reads.sorted.bam
echo "Sorting variant bam file"
samtools sort out/variant_reads.bam > out/variant_reads.sorted.bam

echo "Indexing baseline bam file"
samtools index out/baseline_reads.sorted.bam
echo "Indexing variant bam file"
samtools index out/variant_reads.sorted.bam

echo "Determining gene coverage for baseline reads"
samtools bedcov ngsdata/toy_genome_genes.bed out/baseline_reads.sorted.bam > out/baseline_reads.coverage.txt
echo "Determining gene coverage for variant reads"
samtools bedcov ngsdata/toy_genome_genes.bed out/variant_reads.sorted.bam > out/variant_reads.coverage.txt

echo "Visualizing coverage depth"
python3 visualize.py out/baseline_reads.coverage.txt out/variant_reads.coverage.txt out/results_visualization.png