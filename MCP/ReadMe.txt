pip install PyGithub
pip install mcp

1. Create new file. git_server.py
    Import packages

2. Install NodeJs -> Run using node js since we dont connected to LLM
	npx @modelcontextprotocol/inspector

    if you get issue during command then -> 
    1. powershell -ExecutionPolicy Bypass -NoProfile -Command "npx @modelcontextprotocol/inspector"
    or
    2.
        >Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        >npx @modelcontextprotocol/inspector

Once MCP project executes: Configure
		1. Transport Type : STDIO
		2. Command: python
		3. Argument : pass file path in doble qoute .provide full path including drive
		4. click on Connect
        5. Goto Tools menu
            1.Click -> list_repositories tool we created
            2.Click Run Tool 