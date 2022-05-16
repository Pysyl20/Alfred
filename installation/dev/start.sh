
echo '#################### LANCEMENT EN MODE DEV ####################'

#apt install python3-pip
#pip install --no-cache-dir -r ../../requirements.txt
export FLASK_APP=convert2pdf
export FLASK_ENV=development
python3 ../../app.py
python3 ../../core/startIA.py
