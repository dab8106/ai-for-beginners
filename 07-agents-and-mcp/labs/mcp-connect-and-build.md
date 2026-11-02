# Connect to an MCP server, then build your own

**AI agents, tools and MCP** · Goes with [Lecture 33: MCP (Model Context Protocol) Explained Simply](https://www.youtube.com/watch?v=UpQe27Mo7Ok) and [Lecture 34: Build Your Own MCP Server in Python](https://www.youtube.com/watch?v=kUMFYWrl8WM) and [Lecture 35: Keep AI Agents Safe: Rules Before You Give Them Access](https://www.youtube.com/watch?v=Vi5hXj-Pig8) · About 60 minutes · Some Python, on your own computer

## What you'll do

First you'll connect an AI desktop app to a ready-made MCP server, so the AI can read files in one practice folder. Then you'll run your own small MCP server, written in Python, that lets the AI search a fictional library catalogue. You'll see the host, client and server from the lessons working together.

## What you need

- **A computer** with Windows or macOS. This lab doesn't work on a phone or tablet, because the app has to start programs on your machine.
- An MCP-capable AI app. We use **Claude Desktop** (free download from https://claude.ai/download, sign in with your Claude account). Other apps that support MCP servers work too, such as some code editors with AI assistants; their settings screens differ, but the server and the idea are the same.
- **Python 3.10 or newer**: https://www.python.org/downloads (on Windows, tick "Add python.exe to PATH" in the installer).
- **Node.js** (LTS version) for Part A only: https://nodejs.org. It provides the `npx` command that starts the ready-made server.
- Starter files, in this section's [`starter/`](../starter/) folder:
  - `starter/library_server.py`, your MCP server.
  - `starter/claude_desktop_config.mac.json` and `starter/claude_desktop_config.windows.json`, example settings.

> Safety first, from the lessons: an MCP server can run code and read data on your computer. Only install servers you trust, and give each one only the access it needs. In this lab the file server gets **one practice folder**, never your whole drive, and the library server is read-only.

In the steps below, replace `YOUR-NAME` with your own user folder name. On macOS that's the name shown in Finder next to the house icon; on Windows it's the folder under `C:\Users`.

## Part A: Connect to a ready-made server (20 minutes)

### Step 1: Make a practice folder

Create a folder called `mcp-practice` in your user folder (`/Users/YOUR-NAME/mcp-practice` on macOS, `C:\Users\YOUR-NAME\mcp-practice` on Windows). Inside it, create a text file `todo.txt` with three made-up tasks, for example:

```
Call the Pune vendor about the delayed order
Book a meeting room for Thursday
Send the October sales summary to Priya
```

**Check:** the folder contains only practice files. Nothing private.

### Step 2: Open the app's MCP settings

1. Open Claude Desktop.
2. Open **Settings**, then **Developer**, then **Edit Config**. This opens the folder with `claude_desktop_config.json`. If the file doesn't exist yet, create it.
3. Open the file in a plain text editor (TextEdit in plain-text mode, or Notepad).

### Step 3: Add the file server

Paste in **only the `filesystem` part** of the example config for your system. For macOS it looks like this:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/YOUR-NAME/mcp-practice"]
    }
  }
}
```

On Windows, use the path from `claude_desktop_config.windows.json`. Backslashes in JSON must be doubled: `C:\\Users\\YOUR-NAME\\mcp-practice`.

Save the file and **fully quit** Claude Desktop (not just close the window), then open it again.

**Check:** in a new chat, open the tools or connectors menu near the message box. You should see `filesystem` with a list of tools, such as reading and listing files.

### Step 4: Use it

Ask:

```
What's in my mcp-practice folder? Read todo.txt and turn it into a table
with a column for who or what each task is about.
```

**Check:** the app asks your permission before using a tool. Approve it, and the answer uses the real contents of `todo.txt`. Then ask `Read a file from my Documents folder.` The server should refuse, because it only has access to `mcp-practice`. That's least privilege in action.

## Part B: Build your own server (30 minutes)

### Step 5: Set up a folder and install the MCP package

Create a folder `mcp-library` in your user folder and copy `library_server.py` into it. Then open a terminal (macOS: Terminal; Windows: PowerShell) and run:

**macOS**

```bash
cd ~/mcp-library
python3 -m venv .venv
.venv/bin/pip install mcp
```

**Windows**

```powershell
cd $HOME\mcp-library
py -m venv .venv
.venv\Scripts\pip install mcp
```

**Check:** the last line says `Successfully installed ... mcp-...`.

### Step 6: Read the server code

Open `library_server.py` and find the four parts from the lesson:

1. **The name**: `MCPServer("sahyadri-library")`.
2. **Normal Python functions**: `search_books` and `check_availability`.
3. **The tool marks**: `@mcp.tool()` above each function. The text under each function (its docstring) is the description the model reads.
4. **Run**: `mcp.run(transport="stdio")` at the bottom.

Also notice: no `print()` anywhere. The server talks to the app over standard output, so logs go to standard error with `logging`.

> Older tutorials call the class `FastMCP` and import it from `mcp.server.fastmcp`. That's the same idea in version 1 of the package. The starter file works with both versions.

**Check:** you can say which function the model should use to answer "Is *The Monsoon Ledger* on the shelf?" (first `search_books` to get its ID, then `check_availability`).

### Step 7: Add it to the app

Open `claude_desktop_config.json` again and add a second entry, next to `filesystem`. The command is the **full path to the Python inside your `.venv`**, and the argument is the full path to the server file.

**macOS**

```json
"sahyadri-library": {
  "command": "/Users/YOUR-NAME/mcp-library/.venv/bin/python",
  "args": ["/Users/YOUR-NAME/mcp-library/library_server.py"]
}
```

**Windows**

```json
"sahyadri-library": {
  "command": "C:\\Users\\YOUR-NAME\\mcp-library\\.venv\\Scripts\\python.exe",
  "args": ["C:\\Users\\YOUR-NAME\\mcp-library\\library_server.py"]
}
```

The complete file, with both servers, is in the starter examples. Save, fully quit the app, and open it again.

**Check:** the tools menu now lists `sahyadri-library` with two tools, `search_books` and `check_availability`.

### Step 8: Test it

Ask these in a new chat, approving each tool call:

1. `What books by Ananya Rao does the Sahyadri library have?`
2. `Is Python for Busy People available? If not, when is it due back?`
3. `I'm in Aundh. Can I pick up a cooking book there today?`
4. `Do you have Harry Potter?`

**Check:** question 1 finds two books (SL-105 and SL-107). Question 2 says no copies are available and gives the due-back date, 12 November 2026. Question 3 needs **two** tool calls: a search, then an availability check. Question 4 gets "no books found" from your server, and a good answer says so instead of inventing a copy.

### Step 9: Change a tool and see the effect

Add a new book to `BOOKS` in `library_server.py` (for example, a book by you), save, fully quit and reopen the app, and search for it.

**Check:** the new book is found. Every change to the server needs an app restart, because the app starts the server when it opens.

### If something doesn't work

- **Server not listed**: check the JSON. A missing comma or a single backslash on Windows breaks the whole file. Paste it into any online JSON validator if unsure.
- **Server listed, but with an error**: the paths are usually wrong. Run the exact `command` and `args` from your config in a terminal. If the server starts and waits silently, the path is fine (press Ctrl + C to stop it).
- **Logs**: Claude Desktop keeps MCP log files. On macOS they're in `~/Library/Logs/Claude`, on Windows in `%APPDATA%\Claude\logs`. Your server's `logging` lines appear there.
- **Windows and npx**: if the file server fails to start, change its `"command"` to `"cmd"` and put `"/c", "npx"` at the start of its `args`.
- **Testing without the app (optional)**: the MCP Inspector calls your tools directly, with no AI involved. With Node.js installed, run `npx @modelcontextprotocol/inspector` followed by your Python path and server path, from the `mcp-library` folder.

## Results table

| Test | Tools called, in order | Answer correct? | Did the app ask permission? |
|---|---|---|---|
| Read todo.txt (file server) | | | |
| Read a file outside mcp-practice | | | |
| Books by Ananya Rao | | | |
| Python for Busy People availability | | | |
| Cooking book in Aundh | | | |
| Harry Potter | | | |
| Your new book | | | |

## Stretch challenge

1. **A third tool.** Add `list_subjects()` that returns all subjects in the catalogue, restart, and ask "What kinds of books do you have?"
2. **A risky tool, done safely.** Add `reserve_book(book_id, member_id)` that only **writes a pretend reservation to the log** with `log.info` and returns "Reservation request recorded for staff approval". Think about the lesson "Keeping Agents Safe": why should a person approve real reservations?
3. **A vague description.** Change the `search_books` docstring to just "Search." and see whether the model still uses it well.

## Submit

The filled-in results table, a screenshot of the tools menu showing `sahyadri-library`, and a screenshot of one answer that used `check_availability`. Blur or crop your name and email in screenshots.

## What you learned

- An MCP app (the host) starts each server you list in its settings, and asks it for its tools.
- A ready-made server can give AI controlled access to something real, like one folder. Least privilege decides how much.
- Your own MCP server is a name, a few Python functions marked as tools with clear descriptions, and one line to run it.
- Local servers talk over standard input and output, so they log to standard error, never with print.
