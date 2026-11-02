"""A tiny MCP server for a fictional library catalogue.

dabeer.ai · AI for Beginners · AI agents, tools and MCP

It offers two read-only tools to any MCP app (for example Claude Desktop):
  - search_books:       find books by title, author or subject
  - check_availability: see how many copies of one book are on the shelf

All books, authors and branches are made up for practice.
Run it from an MCP app's settings, not by hand. It talks over standard input
and output, so never use print() here: log to standard error instead.
"""
import logging
import sys

try:
    # Current versions of the official `mcp` Python package (version 2 and later)
    from mcp.server.mcpserver import MCPServer
except ImportError:
    # Older versions (version 1) call the same class FastMCP
    from mcp.server.fastmcp import FastMCP as MCPServer

logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger("library")

# 1. Name the server. This is the name the AI app shows.
mcp = MCPServer("sahyadri-library")

# Practice data: a fictional public library in Pune with two branches.
BOOKS = {
    "SL-101": {"title": "The Monsoon Ledger", "author": "Meera Kulkarni", "subject": "fiction", "year": 2019,
               "copies": {"Kothrud": 2, "Aundh": 0}, "shelf": "F-KUL"},
    "SL-102": {"title": "Python for Busy People", "author": "Arjun Menon", "subject": "programming", "year": 2024,
               "copies": {"Kothrud": 0, "Aundh": 0}, "shelf": "005.13-MEN", "next_due": "2026-11-12"},
    "SL-103": {"title": "Spices of the Deccan", "author": "Farah Siddiqui", "subject": "cooking", "year": 2021,
               "copies": {"Kothrud": 1, "Aundh": 1}, "shelf": "641.5-SID"},
    "SL-104": {"title": "Small Data, Big Decisions", "author": "Rohan Iyer", "subject": "business", "year": 2023,
               "copies": {"Kothrud": 1, "Aundh": 2}, "shelf": "658.4-IYE"},
    "SL-105": {"title": "Machines That Read", "author": "Ananya Rao", "subject": "artificial intelligence", "year": 2025,
               "copies": {"Kothrud": 0, "Aundh": 1}, "shelf": "006.3-RAO"},
    "SL-106": {"title": "Cricket in the Lanes", "author": "Imran Shaikh", "subject": "sport", "year": 2018,
               "copies": {"Kothrud": 3, "Aundh": 1}, "shelf": "796.358-SHA"},
    "SL-107": {"title": "A Gentle Guide to Neural Networks", "author": "Ananya Rao", "subject": "artificial intelligence", "year": 2022,
               "copies": {"Kothrud": 1, "Aundh": 0}, "shelf": "006.32-RAO"},
    "SL-108": {"title": "The Last Train to Lonavala", "author": "Meera Kulkarni", "subject": "fiction", "year": 2024,
               "copies": {"Kothrud": 0, "Aundh": 0}, "shelf": "F-KUL", "next_due": "2026-11-05"},
    "SL-109": {"title": "Gardening on a Balcony", "author": "Leela D'Souza", "subject": "gardening", "year": 2020,
               "copies": {"Kothrud": 2, "Aundh": 2}, "shelf": "635.9-DSO"},
    "SL-110": {"title": "Money Basics for Your First Job", "author": "Kabir Bhatia", "subject": "personal finance", "year": 2025,
               "copies": {"Kothrud": 1, "Aundh": 0}, "shelf": "332.024-BHA"},
}


# 2 and 3. Write normal Python functions, and mark them as tools.
# The docstring becomes the tool's description: the model reads it to decide when to call the tool.
@mcp.tool()
def search_books(query: str) -> list[dict]:
    """Search the Sahyadri Library catalogue by title, author or subject.
    Returns up to 5 matching books with their book IDs. Use check_availability
    with a book ID to see whether copies are on the shelf."""
    q = query.strip().lower()
    log.info("search_books query=%r", q)
    if not q or len(q) > 100:
        return [{"error": "Please give a search word of 1 to 100 characters."}]
    hits = []
    for book_id, b in BOOKS.items():
        if q in b["title"].lower() or q in b["author"].lower() or q in b["subject"].lower():
            hits.append({"book_id": book_id, "title": b["title"], "author": b["author"],
                         "subject": b["subject"], "year": b["year"]})
    return hits[:5] or [{"message": f"No books found for '{query}'."}]


@mcp.tool()
def check_availability(book_id: str) -> dict:
    """Check how many copies of one book are available at each branch (Kothrud and Aundh),
    and its shelf code. If no copies are available, also gives the next due-back date.
    Needs a book ID like SL-101, which you can get from search_books."""
    key = book_id.strip().upper()
    log.info("check_availability book_id=%r", key)
    if key not in BOOKS:
        return {"error": f"No book with ID '{book_id}'. IDs look like SL-101."}
    b = BOOKS[key]
    result = {"book_id": key, "title": b["title"], "available": b["copies"],
              "total_available": sum(b["copies"].values()), "shelf": b["shelf"]}
    if result["total_available"] == 0:
        result["next_due_back"] = b.get("next_due", "unknown")
    return result


# 4. Run the server. "stdio" means it talks to the app over standard input and output.
if __name__ == "__main__":
    log.info("Sahyadri library MCP server starting")
    mcp.run(transport="stdio")
