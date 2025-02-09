from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

student_marks = [{"name":"yGo9VR","marks":24},{"name":"tH228il","marks":84},{"name":"JguHbkK1","marks":63},{"name":"rGd2ZK","marks":4},{"name":"vh2sL3BH9W","marks":2},{"name":"AnMwpnlENL","marks":67},{"name":"m","marks":6},{"name":"o","marks":87},{"name":"wSsS","marks":48},{"name":"6Q","marks":47},{"name":"yDtBLDdMe","marks":4},{"name":"TzfowE0jSJ","marks":74},{"name":"rLfn","marks":39},{"name":"5S4MS","marks":89},{"name":"u3pjmrh","marks":48},{"name":"q","marks":58},{"name":"3WZxZT","marks":61},{"name":"rbZPct","marks":93},{"name":"4TbmEv","marks":37},{"name":"PFECfZBFA","marks":39},{"name":"K7IG","marks":57},{"name":"6dfHbYg","marks":57},{"name":"eiWLZ","marks":80},{"name":"7B9lBtUWJW","marks":27},{"name":"j62","marks":61},{"name":"c5yn","marks":4},{"name":"YNDxMWOe1e","marks":4},{"name":"V","marks":6},{"name":"fALc2aINXR","marks":0},{"name":"v4","marks":89},{"name":"rK7HI6j","marks":37},{"name":"s8yN7wZ","marks":99},{"name":"ZBj2","marks":96},{"name":"t","marks":53},{"name":"34Wly","marks":31},{"name":"yESlvJ","marks":49},{"name":"sb8","marks":66},{"name":"qxC","marks":92},{"name":"kbplYTT","marks":99},{"name":"x1ntso","marks":26},{"name":"RIy2s6","marks":25},{"name":"PUl","marks":24},{"name":"Ft","marks":36},{"name":"SwAtvhD0","marks":95},{"name":"8hSJ7Jo","marks":53},{"name":"D9","marks":45},{"name":"tTT3","marks":68},{"name":"l6mXbk1dC","marks":40},{"name":"Nl3RjBd2","marks":64},{"name":"J3xHni","marks":57},{"name":"nuiULZC","marks":74},{"name":"kXnrxB","marks":82},{"name":"pO","marks":71},{"name":"GIQoEPWw","marks":67},{"name":"toHpNd","marks":22},{"name":"v","marks":48},{"name":"n2OBZL","marks":85},{"name":"tp2vJg9C","marks":89},{"name":"Ls3YCE","marks":4},{"name":"x","marks":84},{"name":"xzL2lpP","marks":86},{"name":"glsNa","marks":45},{"name":"f5zXk7Yd","marks":85},{"name":"4lTOzMLD","marks":96},{"name":"egYI","marks":55},{"name":"JEa4","marks":63},{"name":"aHWAObTm","marks":83},{"name":"fIeSh6dly3","marks":64},{"name":"i7e","marks":50},{"name":"mxhxvZVYe","marks":48},{"name":"c0Br","marks":76},{"name":"KyOf","marks":58},{"name":"y3LM","marks":61},{"name":"EwmtyM","marks":15},{"name":"XQbgS","marks":60},{"name":"jeGxE","marks":98},{"name":"6zZ1Ph8","marks":91},{"name":"tbSGK","marks":10},{"name":"eCt","marks":50},{"name":"P3","marks":11},{"name":"c11CaRit","marks":95},{"name":"bkMEcPq","marks":87},{"name":"cznOiec","marks":41},{"name":"Mws","marks":15},{"name":"bOOL","marks":4},{"name":"Z","marks":50},{"name":"vJd45If","marks":11},{"name":"MN","marks":67},{"name":"9CADQdLaHk","marks":77},{"name":"s9m9","marks":96},{"name":"ifPV","marks":21},{"name":"VHbH7XRK","marks":29},{"name":"aV","marks":91},{"name":"H8cKfL","marks":89},{"name":"d","marks":93},{"name":"6","marks":9},{"name":"c","marks":63},{"name":"b83C","marks":88},{"name":"4d8","marks":48},{"name":"uBApl0t","marks":95}]

@app.get("/api")
async def get_marks(name: list[str] = Query(default=None)):
    """
    Fetch marks for the specified student names.
    If no names are provided, an empty list of marks is returned.
    """
    if names:
        result = [student["marks"] for student in student_marks if student["name"] in name]
        return {"marks": result}
    
    return {"marks": []}
