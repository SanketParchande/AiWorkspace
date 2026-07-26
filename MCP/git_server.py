from mcp.server.fastmcp import FastMCP
from github import Github
from access_git_token import git_token  # Import the token from token.py

mcp = FastMCP("GitHub") #app instance
github = Github(git_token) #connected to github

@mcp.tool() # decorator to register the function as a tool in the app
def list_repositories():
    """List my GitHub repositories."""
    user = github.get_user()    #Getting he user account using token 
    return [repo.name for repo in user.get_repos()] # get/fetch all the repositories and return the names of the repositories in a list

mcp.run() #run the app