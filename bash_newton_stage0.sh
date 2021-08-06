#!/bin/bash
# HACKBIO INTERNSHIP 2021
# TEAM #Newton
## STAGE 0
## PROGRAM LOGIC FOR BASH SCRIPT
#	A shell script to clone to
#	* check for script dependencies to run each submitted script
#	* clone the team's GitHub repository () to home folder of administrator
#	* execute all scripts in assigned folder
#	* create a csv file to hold script outputs
	TEAM_REPO="https://github.com/akinmode/TeamNewton_HackBio2021.git"
	NEWTON_FOLDER="TeamNewton_HackBio2021/scripts_stage_0"
	OUTPUT_CSV="team_newton_stage_0.csv"
echo "=============================================================="
echo "CLONING TEAM NEWTON REPOSITORY @ GITHUB ..."
	git clone $TEAM_REPO
echo " "
echo "=============================================================="
echo "CHECKING FOR REQUIRED DEPENDECIES ..."
	REQ_DEPEND=("bash" "python3" "julia")
echo "[INFO] The Following are required to run the submitted scripts: "${REQ_DEPEND[@]}
	for i in "${REQ_DEPEND[@]}";do
	    command -v $i >/dev/null 2>&1 || {
	        echo >&2 "[CHECK]: $i package is required to run the submitted scripts";
		echo "[CHECK]: Install '$i package'and rerun";
	        exit 1;
	    }
	done
echo "[INFO] All required packages are available on local machine"
echo " "
echo "==============================================================="
echo "HACKBIO INTERNSHIP 2021: TEAM Newton"
_generate() {
	#Create a csv file with the header
	echo "[INFO] Creating csv for submitted scripts to "$OUTPUT_CSV
	echo "NAME,EMAIL,SLACK HANDLE,BIOSTACK,TWITTER HANDLE,HAMMING DISTANCE" > $OUTPUT_CSV
	echo " "
	#Loop through the designated folder to run the scripts beginning with 'newton'
	for i in $NEWTON_FOLDER/newton_*;do
	    case $i in
		*".sh" ) bash $i | awk -F":" '{ORS=","}{print $2}' | sed 's/,$/\n/g' >> $OUTPUT_CSV; echo "[INFO] "$(basename -- $i) " extracted to "$OUTPUT_CSV;;
      	*".py" ) python3 $i | awk -F":" '{ORS=","}{print $2}' | sed 's/,$/\n/g' >> $OUTPUT_CSV; echo "[INFO] "$(basename -- $i) " extracted to "$OUTPUT_CSV;;
		*".jl" ) julia $i | awk -F":" '{ORS=","}{print $2}' | sed 's/,$/\n/g' >> $OUTPUT_CSV; echo "[INFO] "$(basename -- $i) " extracted to "$OUTPUT_CSV;;
		*".R" ) Rscript $i | awk -F":" '{ORS=","}{print $2}' | sed 's/,$/\n/g' >> $OUTPUT_CSV; echo "[INFO] "$(basename -- $i) " extracted to "$OUTPUT_CSV;;
   		esac
	done
	echo " "
	echo "[INFO] "$OUTPUT_CSV" generated!"
}
_generate
echo "[SUCCESS]TASK COMPLETED FOR TEAM NEWTON!"
