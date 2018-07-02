# simulations for delta likelihood

for meandepth in 100;
    do

    for base_ploidy in 4 5;
        do

        for no_of_aneu in 1 2 3 4;
            do

            for aneu_level in 1 2 3 4 5;
                do
                
                    for i in `seq 1 10`;
                        do  
                            NSAMS=$((5 + RANDOM % 6))
                            input=${base_ploidy}x$((${NSAMS}-${no_of_aneu})),${aneu_level}x${no_of_aneu}
                            echo $input
                            bash Test_data_sim.sh $meandepth $input $i $NSAMS
                            python Geno_Likes_simul_delta.py ../Data/Data_sims/${i}_T$input.mpileup.gz ../Data/Data_sims/${i}_T$input.genolikes.gz ../Data/Data_sims/${i}_T$input.ploids.gz $NSAMS
                            rm ../Data/Data_sims/${i}_T$input.genolikes.gz 
                            rm ../Data/Data_sims/${i}_T$input.ploids.gz
                            rm ../Data/Data_sims/${i}_T$input.mpileup.gz
                        done
                done
            done
        done
    done







