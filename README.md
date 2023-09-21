# DonationPlatform
This is an open-source project of donate platform API built on Smart Contract &amp; Python API.


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
 
