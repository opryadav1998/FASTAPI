from fastapi import FastAPI
import uvicorn
from calculate import calculate
from restapi_model import user_input

    
app = FastAPI(
	docs_url="/",
	title="Price Science Workbench",
	description="Backend solution for Price Science Workbench operations",
	version="0.0.4",
)

@app.post("/calculate")
def operate(input: user_input):
    result = calculate(input.operation, input.x, input.y)   
    return result

@app.post("/tablenames")
def operate(input: str):
    result = calculate(input.operation, input.x, input.y)   
    return result



if __name__ == "__main__":
	port = 8000
	print(f"Starting server on port {port}")
	uvicorn.run(app, host="localhost", port=port)
