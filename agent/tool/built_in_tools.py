from langchain_community.tools import DuckDuckGoSearchRun, ShellTool, YouTubeSearchTool

search_tool = DuckDuckGoSearchRun()
shell_tool = ShellTool()
youtube_tool = YouTubeSearchTool()


print(search_tool.invoke("Bangladesh"))
print(shell_tool.invoke("dir"))
print(youtube_tool.invoke("cóunter"))
