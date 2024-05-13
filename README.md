## Running Picking App Frontend

1) Install nvm and node
2) Run `node --version` and confirm that it is node version 18 > 
   1) If it is version 16 let's say you can run `nvm use 18` For this project I used
   v18.19.0
3) Install angular CLI: `npm install -g @angular/cli`
4) Go into root directory of picking-app-ui and run `npm install`
5) Run `npm run start` and you should be able to see the project on `http://localhost:4200`

## Running Picking App Backend

1) Head to root of picking-app-backend
2) Install Python3 and pip3 if you haven’t already. 
3) Create and activate virtual environment (optional) 
4) `pip3 install -r requirements.txt`
5) Make sure PYTHONPATH points to `${ROOT_DIR}/app`
   1) You can do something like: `export PYTHONPATH=$PWD/app`
6) You can cd into app folder and run `fastapi run main.py`

Note: for python3 I ran project on version: `3.8.2`