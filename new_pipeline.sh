#!/bin/bash
#SBATCH --job-name=new_pipeline_
#SBATCH --ntasks-per-node=12
#SBATCH --time=24:0:0
#SBATCH --output=new_pipeline_.out
#SBATCH --error=new_pipeline_.err
#SBATCH --mail-user=largentl@oregonstate.edu
#SBATCH --mail-type=END

python new_pipeline.py > new_pipeline.txt