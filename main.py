from fastapi import FastAPI
from models.project import ProjectCreateRequest, ProjectCreateResponse, ProjectHelper

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/create-project/", response_model=ProjectCreateResponse)
async def create_project(project_data: ProjectCreateRequest):
    response = ProjectHelper.create_project(project_data)
    return response


@app.get("/get-owner/")
async def get_owner():
    response = ProjectHelper.get_owner()
    return response


@app.get("/get-projects/")
async def get_projects():
    response = ProjectHelper.get_projects_ids()
    return response


@app.get("/get-project/{project_id}")
async def get_project(project_id: int):
    response = ProjectHelper.get_project(project_id)
    return response


@app.post("/close-project/{project_id}")
async def close_project(project_id: int):
    response = ProjectHelper.close_project(project_id)
    return response


@app.post("/withdraw-funds-to-owner/{project_id}")
async def withdraw_to_project_owner(project_id: int):
    response = ProjectHelper.withdraw_to_project_owner(project_id)
    return response



# {
#   "title": "New Project",
#   "description": "The new cool project",
#   "owner": "0xC162C51C1735E6e29CC7f932AADb0FeEB20a369D",
#   "date_expiration": 1697627008,
#   "project_goal": 100000
# }
