#!/bin/bash# Create project structure
echo "Creating src directory"
mkdir -p src

echo "Entering src directory"


echo "Creating .py files"
touch src/data_analysis.py
touch src/data_analysis_functions.py


echo "creating data directory"
mkdir -p data
echo "creating csv file"
touch data/students.csv

cat > data/students.csv << 'EOF'
name,age,grade,subject
one, 20, 92, math
two, 30, 78, science
three, 21, 80, trig
four, 27, 88, calculus
five, 32, 95, chemistry
six, 40, 67, biology
seven, 19, 55, atronomy
eight, 18, 90, calculus
EOF


echo "creating output directory"
mkdir -p output
touch .gitignore
touch requirements.txt





