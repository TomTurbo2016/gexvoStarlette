from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn
import time

app = Starlette(debug=True)

@app.route('/')
async def homepage(request):
    time.sleep(10)
    return JSONResponse({'hello': 'world'})
	
	
if __name__ == '__main__':
	if 'serve' in sys.argv: uvicorn.run(app=app, host='0.0.0.0', port=5042)
