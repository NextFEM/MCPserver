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
# rebar dimensioning for concrete members
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
def get_selected_elements()->list:
    return nf.selectedElements
def set_selected_elements(elems:list):
    nf.selectedElements = elems
def get_selected_nodes()->list:
    return nf.selectedNodes
def set_selected_nodes(nodes:list):
    nf.selectedNodes = nodes
mcp.tool(name="selectedElements")(refresh_after(get_selected_elements))
mcp.tool(name="selectElements")(refresh_after(set_selected_elements))
mcp.tool(name="selectedNodes")(refresh_after(get_selected_nodes))
mcp.tool(name="selectNodes")(refresh_after(set_selected_nodes))
mcp.tool(name="elemsList")((lambda: nf.elemsList))
mcp.tool(name="nodesList")((lambda: nf.nodesList))
mcp.tool(name="materialsID")((lambda: nf.materialsID))
mcp.tool(name="sectionsID")((lambda: nf.sectionsID))


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')