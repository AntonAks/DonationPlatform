from fastapi import FastAPI, Request
from models.project import ProjectCreateRequest, ProjectCreateResponse, ProjectHelper
from fastapi.templating import Jinja2Templates


app = FastAPI(
    title="Donation platform API",
    description="Donation platform REST API on Ethereum blockchain",
    version="1.0.0",
    openapi_url="/openapi.json",  # Customize the URL of your OpenAPI schema
)


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):

    projects_ids = ProjectHelper.get_projects_ids()
    projects_for_template = []

    for projects_id in projects_ids[:5]:
        projects_for_template.append(ProjectHelper.get_project(projects_id))

    return templates.TemplateResponse("index.html", {"request": request, "data": projects_for_template})


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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
