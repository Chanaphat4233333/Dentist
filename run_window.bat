@echo off
echo Starting Data Processor...

call dentist-env\Scripts\activate

python app.py

exit