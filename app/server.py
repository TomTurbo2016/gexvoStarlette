import os
import sys
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse, PlainTextResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn, aiohttp, asyncio
from io import BytesIO
import time
from starlette.templating import Jinja2Templates



####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~To-Be-Edited~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#DOWNSIZE_INPUT_IMAGE = 400 #--> 255 px: Downsize uploaded Image (cv2 Image)
PATH_TO_BASE64_TXT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/base64strings/')
#PATH_TO_STYLE_FILES = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/styleModels/')
#PATH_TO_SCALE_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/upscaleModel/')
PATH_TO_TEMPLATES = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'view/')
templates = Jinja2Templates(directory=PATH_TO_TEMPLATES)
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))


####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~>
async def LongRunningFunction():
	time.sleep(10)
	return 'finished'

async def setup_LongRunningFunction():
	result = await LongRunningFunction()
	return result
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_LongRunningFunction())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()


@app.route('/')
def index(request):
	return templates.TemplateResponse('index.html', {'request': request})

@app.route('/upload', methods=['POST'])
async def upload(request):
	if request.method == "POST":
		await setup_LongRunningFunction()
		data = 'Hello World 1'
		return PlainTextResponse(data)

@app.route('/showPic', methods=['GET', 'POST'])
async def ShowPic(request):
	if request.method == 'GET':
		data = 'Hello World 1'
		return PlainTextResponse(data)
	else:
		data = 'Hello World 2'
		return PlainTextResponse(data)

