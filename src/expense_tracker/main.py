import random
from fastmcp import FastMCP


mcp = FastMCP(name='Demo server')

@mcp.tool
def roll_dice(n_dice:int):
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add(a:int, b:int):
    return a+b

if __name__ == '__main__':
    mcp.run()
