import uvicorn
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse, Response

from fastapi.middleware.cors import CORSMiddleware
from programs.video_play import play_video
from programs.video_stack import stack_video
from programs.coach import track_video
import os
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# convert list into tuple
def convert_list_tuple(list):
    return tuple(list)

CHUNK_SIZE = 1024*1024

# Image List Table
headings = ("Image_Name", "Display", "Delete")
data = () 

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request} )

@app.get("/videolist")
def list_file(request: Request):

    files = os.listdir("static/videos")
    file_path = files[0]

    return templates.TemplateResponse("list_video.html", {"request": request, "files":files, "myImage": file_path})

@app.get("/uploadvideo")
def list_file(request: Request):

    return templates.TemplateResponse("upload_video.html", {"request": request})

@app.post("/uploadvideo/", response_description="video uploaded and stored in static/videos folder")
async def create_upload_files(request: Request, file: UploadFile = File(...)):
    
    file_name = file.filename
    file_path = f"static/videos/" + file_name
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    #result = await play_video(file_path)
        
    return ("uploaded at /" + file_path)


""" 
VIDEO Playing 
"""  
@app.post("/uploadplay/", response_description="Image uploaded and data added into the database")
async def create_upload_video(file: UploadFile = File(...)):
    
    file_name = file.filename
    file_path = f"static/videos/" + file_name
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    play_video(file_path)
    
    return()
 
@app.get("/videoplay/{id}")
async def read_files(request: Request, id: str, q: str | None = None):
    file_type= id.split(".")[1]
    mediatype ='video/'+ file_type
    print(mediatype)
    file_path = Path("static/videos/" + id)

    return FileResponse(file_path)
""" 
VIDEO STacking 
"""

@app.post("/uploadfiles/", response_description="Image uploaded and data added into the database")
async def create_upload_files(files: list[UploadFile] = File(...)):
    file_names = []
    file_paths = []
    
    for file in files:
        file_name = file.filename
        file_type = file_name.split(".")[1]
        file_names.append(file_name)
        file_path = f"static/videos/" + file_name
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_paths.append(file_path)
    result = await stack_video(file_paths)
    
    return("stacked video stored as path /" + result)

    
@app.get("/videostack")
async def main():
    content ="""
<body>
<form action="uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
"""
    return HTMLResponse(content=content)

""" 
VIDEO Tracing 
"""   
    
@app.post("/uploadvideo/", response_description="Image uploaded and data added into the database")
async def create_upload_video(file: UploadFile = File(...)):
    
    file_name = file.filename
    file_path = f"static/videos/" + file_name
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    result = await track_video(file_path)
   
              
@app.get("/videotrace")
async def main():
    content ="""
<body>
<form action="videotrace/" enctype="multipart/form-data" method="post">
<input name="file" type="file">
<input type="submit">
</form>
</body>
"""
    return HTMLResponse(content=content)

@app.post("/videotrace/", response_description="Image uploaded and data added into the database")
async def create_upload_video(file: UploadFile = File(...)):
    
    file_name = file.filename
    file_path = f"static/videos/" + file_name
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    result = await track_video(file_path)
    result = file_path
    return("tracing result", result)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port = 5000, reload=True)