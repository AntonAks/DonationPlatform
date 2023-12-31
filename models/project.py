from pydantic import BaseModel
import json
from settings import contract, w3, OWNER_ADDRESS, PRIVATE_KEY
from hexbytes import HexBytes


class ProjectCreateRequest(BaseModel):
    title: str
    description: str | None = None
    owner: str
    date_expiration: int
    project_goal: int


class ProjectCreateResponse(BaseModel):
    message: str
    transaction: str


class ProjectHelper:

    @staticmethod
    def create_project(project_data: ProjectCreateRequest):
        # Extract data from the ProjectCreateRequest
        project_title = project_data.title
        project_owner = project_data.owner
        project_goal = project_data.project_goal
        date_expiration = project_data.date_expiration

        nonce = w3.eth.get_transaction_count(OWNER_ADDRESS)

        chain_id = w3.eth.chain_id

        # Call your function
        call_function = contract.functions.createProject(
            project_title,
            project_owner,
            project_goal,
            date_expiration
        ).build_transaction(
            {"chainId": chain_id, "from": OWNER_ADDRESS, "nonce": nonce})

        # Sign transaction
        signed_tx = w3.eth.account.sign_transaction(call_function, private_key=PRIVATE_KEY)

        # Send transaction
        send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
        hex_bytes = tx_receipt.get('transactionHash')
        return {"message": "Project created",
                "transaction": hex_bytes.hex()}

    @staticmethod
    def close_project(project_id: int):
        nonce = w3.eth.get_transaction_count(OWNER_ADDRESS)

        chain_id = w3.eth.chain_id

        # Call your function
        call_function = contract.functions.closeProject(project_id).build_transaction(
            {"chainId": chain_id, "from": OWNER_ADDRESS, "nonce": nonce})

        # Sign transaction
        signed_tx = w3.eth.account.sign_transaction(call_function, private_key=PRIVATE_KEY)

        # Send transaction
        send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
        hex_bytes = tx_receipt.get('transactionHash')

        return {"message": "Project closed",
                "transaction": hex_bytes.hex()}

    @staticmethod
    def withdraw_to_project_owner(project_id: int):
        nonce = w3.eth.get_transaction_count(OWNER_ADDRESS)

        chain_id = w3.eth.chain_id

        # Call your function
        call_function = contract.functions.withdrawToProjectOwner(project_id).build_transaction(
            {"chainId": chain_id, "from": OWNER_ADDRESS, "nonce": nonce})

        # Sign transaction
        signed_tx = w3.eth.account.sign_transaction(call_function, private_key=PRIVATE_KEY)

        # Send transaction
        send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
        hex_bytes = tx_receipt.get('transactionHash')

        return {"message": "All funds withdrawn to project owner",
                "transaction": hex_bytes.hex()}

    @staticmethod
    def get_owner():
        return contract.functions.owner().call()

    @staticmethod
    def get_projects_ids():
        return contract.functions.getProjectIds().call()

    @staticmethod
    def get_project(project_id: int):
        project_data = contract.functions.getProject(project_id).call()
        _project = dict()
        _project['project_id'] = project_data[0]
        _project['project_title'] = project_data[1]
        _project['project_owner'] = project_data[2]
        _project['project_goal'] = project_data[3]
        _project['project_expiration'] = project_data[4]
        _project['project_balance'] = project_data[5]
        _project['project_is_open'] = project_data[6]
        return _project
