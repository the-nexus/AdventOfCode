#!/bin/bash

# Read user input
read -p "Enter the year of the problem (eg. '2018'): " year
if [[ -z "$year" ]]; then
    echo "Invalid input. Process exited."
    exit 1
fi

read -p "Enter the day of the problem (eg. '04'): " day
if [[ -z "$day" ]]; then
    echo "Invalid input. Process exited."
    exit 1
fi

templateDir=./Utilities/DayN/
templateName=DayN
targetDir=./$year/day$day/
targetName=Day$day
echo ""

# Make sure the directory doesn't exist (prevent overwriting) before creating it
if [[ -d $targetDir ]]; then
    echo "Directory '$targetDir' already exists. Delete it before running this script."
    exit 1
fi
echo "Creating directory '$targetDir'..."
mkdir $targetDir
echo ""

# Copy the template files to the target directory
echo "Copying files from '$templateDir' to '$targetDir'..."
cp $templateDir* $targetDir
echo ""

# Move to the target directory to make the work easier
cd $targetDir

# Rename the copied template file to the specified day value
echo "Renaming files copied files..."
for fileName in *; do
    newFileName=${fileName/$templateName/$targetName}
    mv ./$fileName ./$newFileName
    echo "    '$fileName' was renamed to '$newFileName'"
done
echo ""

# Replace all occurences of the template in the file's data
echo "Adjusting data in files..."
for fileName in *; do
    sed -i -e "s/$templateName/$targetName/g" $fileName
    echo "    '$fileName' was adjusted"
done
echo ""

#Return to the initial directory and exit
cd $initialDir
echo "...Done!"
exit 0