# DonationPlatform
This is an open-source project of donate platform API built on Smart Contract &amp; Python API.

## Idea description
The idea of this project is to create a donation platform where people can donate money to a specific cause.
The platform will be built on top of a smart contract that will be deployed on the Ethereum blockchain.
The platform will have a web interface where users can see all the causes and donate to them.
The platform will have a backend API that will be used by the web interface to get all the data from the blockchain.

### Basic workflow
1. User creates a project with a goal - funds that he/she wants to collect. And start to promote his project. 
2. Donors connect their wallets to the UI and send money to project
3. When goal is achieved, project closes and all funds that were received sends to the Project owner wallet (it can be not a creator of project)
4. Also, project can be closed in case if project's expiration time in ended. In this case, Project creator can decide - send money to the target wallet or send them back to the donors. 


## Project Structure

1. Root dir - Fast API server
2. `./contracts` - Solidity Smart Contract
3. `./models` - Main API models and backend logic
4. ./main.py - Fast API server entry point with all project routes


## How to run
1. Install Python 3.10 or higher
2. In root dir, run commands:
   - Install virtualenv - `virtualenv -p /usr/local/bin/python3.11 venv`
   - Activate virtualenv - `source venv/bin/activate` 
   - run command -  `pip install -r requirements.txt`
   - run command - `uvicorn main:app --reload`
3. Open browser and go to `http://127.0.0.1:8000/docs`
4. Create a local_settings.py file and create a main settings variables there:
   - `CONTRACT_ADDRESS` - Address of deployed smart contract
   - `PRIVATE_KEY` - Private key of contract owner
   - `OWNER_ADDRESS` - Address of contract owner
   - `WEB3_PROVIDER_URL` - URL of web3 provider with user key
5. Depending on the smart contract version you might need to change the `contract_abi.json` file in the root dir.
 
