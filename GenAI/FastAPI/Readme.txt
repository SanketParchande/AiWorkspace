Create env
     python -m venv myenv      
Install library
    #pip install fastapi
    #pip install uvicorn
    #pip install pydantic
    #pip install dotenv
    #pip install anthropic


#if issue appears during activation of env related signed key: 
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass .\myenv\Scripts\Activate.ps1


To Run the app in env:
    uvicorn claude:app --reload
    Launch browser route to http://localhost:8000/docs to see swagger view of Fast API's
