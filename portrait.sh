if ! command -v nvm &> /dev/null
then
    curl -sL https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh -o install_nvm.sh
    bash install_nvm.sh
    rm install_nvm.sh
    nvm install v14.18.0
fi

if  [ -d "venv" ] 
then
# nothing
else
    python3 -m venv venv
fi

. venv/bin/activate
nvm use  v14.18.0

if ! command -v squoosh-cli &> /dev/null
then
    npm i -g @squoosh/cli
fi


# run the script
python3 main_portrait.py