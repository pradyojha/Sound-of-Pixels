#!/bin/bash

OPTS=""
OPTS+="--mode eval "
OPTS+="--id MUSIC-2mix-LogFreq-resnet18dilated-unet7-linear-frames3stride24-maxpool-binary-weightedLoss-channels32-epoch100-step40_80 "
OPTS+="--list_val /data/pojha/research-data/Sound-of-Pixels/val.csv "
OPTS+="--list_train /data/pojha/research-data/Sound-of-Pixels/train.csv "

# Models
OPTS+="--arch_sound unet7 "
OPTS+="--arch_synthesizer linear "
OPTS+="--arch_frame resnet18dilated "
OPTS+="--img_pool maxpool "
OPTS+="--num_channels 32 "
# binary mask, BCE loss, weighted loss
OPTS+="--binary_mask 1 "
OPTS+="--loss bce "
OPTS+="--weighted_loss 1 "
# logscale in frequency
OPTS+="--num_mix 2 "
OPTS+="--log_freq 1 "

# frames-related
OPTS+="--num_frames 3 "
OPTS+="--stride_frames 24 "
OPTS+="--frameRate 8 "

# audio-related
OPTS+="--audLen 65535 "
OPTS+="--audRate 11025 "

#python3 -m pdb main.py $OPTS
#source /export/apps/anaconda3-gpu/etc/profile.d/conda.sh
conda activate base
# if you face libstd++ or libgcc issue , install addtional conda packages in the prerequistes.txt for libstd and libgcc 
# and enable the below line as appropiate with the path
export LD_LIBRARY_PATH=/home/pojha/.conda/envs/py36/lib/:$LD_LIBRARY_PATH
python main.py $OPTS
conda deactivate
