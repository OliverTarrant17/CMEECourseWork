mpileup=$1
NSAMS=$2
stem=${mpileup%'.mpileup.gz'}
genolikes=${stem}.genolikes.gz
ploids=${stem}.ploids.gz
plot=${stem}.plot.pdf




python Geno_like_aneu_test_ANN.py $mpileup $genolikes $ploids $NSAMS

/usr/lib/R/bin/Rscript --verbose Visualise.R $genolikes $ploids $plot $NSAMS
