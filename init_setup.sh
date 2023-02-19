echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8 version"
conda create --name ppd python=3.8 -y
echo [$(date)]: "Activating the environment"
source activate ppd
echo [$(date)]: "Installing the dev env"
pip install -r requirements.txt
echo [$(date)]: "Installing prediction env"
#pip install -r prediction_service/requirements_dev.txt
echo [$(date)]: "END"