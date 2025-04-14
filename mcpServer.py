import mcp
from mcp.server.fastmcp import FastMCP
from nextfempy import NextFEMrest
from functools import wraps

# Initialize FastMCP
mcp = FastMCP("NextFEM")
nf=NextFEMrest(_msg=False)

# Decorator to refresh view after each operation
def refresh_after(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        nf.refreshDesignerView(2,True)
        return result
    return wrapper

# tools
mcp.tool()(refresh_after(nf.addNodeWithID))
mcp.tool()(refresh_after(nf.addBeam))
mcp.tool()(refresh_after(nf.addTria))
mcp.tool()(refresh_after(nf.meshAreaTria))
mcp.tool()(refresh_after(nf.addQuad))
mcp.tool()(refresh_after(nf.meshQuad2Wall))
mcp.tool()(refresh_after(nf.addMatFromLib))
mcp.tool()(refresh_after(nf.addIsoMaterial))
mcp.tool()(refresh_after(nf.assignSectionToElement))
mcp.tool()(refresh_after(nf.assignMaterialToElement))
mcp.tool()(refresh_after(nf.getNodeCoordinates))
# rebar dimensionning for concrete members
mcp.tool()(refresh_after(nf.addLongitRebar))
mcp.tool()(refresh_after(nf.addDesignMatFromLib))
mcp.tool()(refresh_after(nf.addStirrupBars))

# sections
mcp.tool()(refresh_after(nf.addRectSection))
mcp.tool()(refresh_after(nf.addCircSection))
mcp.tool()(refresh_after(nf.addLSection))
mcp.tool()(refresh_after(nf.addTSection))
mcp.tool()(refresh_after(nf.addDTSection))
mcp.tool()(refresh_after(nf.addPlanarSection))
# properties
mcp.tool(name="selectedElements")(lambda: nf.selectedElements)
mcp.tool(name="selectedNodes")(lambda: nf.selectedNodes)
mcp.tool(name="elemsList")(lambda: nf.elemsList)
mcp.tool(name="nodesList")(lambda: nf.nodesList)
mcp.tool(name="materialsID")(lambda: nf.materialsID)
mcp.tool(name="sectionsID")(lambda: nf.sectionsID)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')