#!/bin/sh

SERIES=s01 # specify series i.e. channel here
PARALLEL_JOBS=6 # optimal value depends on available RAM and [voxel] size of images; unlikely to be limited by number of available CPU cores
TEMPORAL_WINDOW=5 # default (maximal) temporal window for logical rules in TGMM
OUTPUT_FOLDER=~/Downloads/TGMM_output # temporary TGMM output, ensure enough free space here
# NOTE: TGMM output will be copied to current directory at the end of the script!

#extract list of numbers for timepoints
my_array=($(ls *$SERIES.klb | perl -ne 's/t00(\d+)_'"$SERIES"'.klb/$1/;print if /^\d+$/;'))
#echo "${my_array[*]}"
len=${#my_array[@]}


#update tgmm_config.txt with folder location
echo "Updating tgmm.config.txt and running ProcessStack and TGMM from $start to $stop"
this_pwd=`pwd`

sed -i 'imgFilePattern=/d' tgmm_config.txt
sed -i 'debugPathPrefix=/d' tgmm_config.txt
echo imgFilePattern=$this_pwd/t00???_$SERIES >> tgmm_config.txt
echo debugPathPrefix=$OUTPUT_FOLDER >> tgmm_config.txt

#adjust temporal window if needed, then append config file
if [ $len -lt $((4 * $TEMPORAL_WINDOW)) ]
then
	TEMPORAL_WINDOW=$(($len/4))
fi

sed -i 'temporalWindowForLogicalRules=/d' tgmm_config.txt
sed -i 'SLD_lengthTMthr=/d' tgmm_config.txt
echo temporalWindowForLogicalRules=$TEMPORAL_WINDOW >> tgmm_config.txt
echo SLD_lengthTMthr=$TEMPORAL_WINDOW >> tgmm_config.txt

#if command is only for update, terminate script here
if [ "$1" = "update" ]; then
    exit 0
fi


#make sure we have enough timepoints represented to even begin
if [ $len -gt 2 ]
then

	#clear last run log
	rm tgmm_complete_run.log
	
	#clear out current binCDTWfeatures and GMEMtracking
	mkdir binCDTWfeatures_flush
	mkdir GMEMtracking3D_flush
	mv -f /opt/tgmm/binCDTWfeatures/* binCDTWfeatures_flush/
	mv -f $OUTPUT_FOLDER/GMEMtracking3D_* GMEMtracking3D_flush/
	
	#remove leading zeros
	start=$(echo ${my_array[0]} | sed 's/^0*//')
	if [ -z $start ]
	then
		start=0
	fi
	stop=$(echo ${my_array[($len-1)]} | sed 's/^0*//')	
	
	#do ProcessStack
	parallel --delay 40 --jobs $PARALLEL_JOBS /opt/tgmm/bin/ProcessStack tgmm_config.txt {} >> tgmm_complete_run.log 2>&1 ::: $(seq $start $stop)

    #do TGMM
	mkdir $OUTPUT_FOLDER
	/opt/tgmm/bin/TGMM tgmm_config.txt $start $stop >> tgmm_complete_run.log 2>&1
	
	#copy binCDTWfeatures and GMEMtracking here
	mkdir binCDTWfeatures
	mv -f /opt/tgmm/binCDTWfeatures/* binCDTWfeatures/
	mv -f $OUTPUT_FOLDER/GMEMtracking3D_* .
	rm -rf $OUTPUT_FOLDER
fi


 
