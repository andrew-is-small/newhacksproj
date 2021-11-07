# Documentation

of the backend xd

Serves on the default http://127.0.0.1:5000/ page

### To fetch information
- To fetch all data about a task, send a request to /alldata/[taskid]
- To fetch basic data about a task, send a request to /basicdata/[taskid]

### To execute commands
Send a post request to /[method], with relevant fields.

### Commands(post reqest)

Command name is in quotes eg. "createtask". Keys required in the post request are detailed
below it in bullet points.

"createtask":
creates a new task(project task or daily task). Args required:
- type: type of task(project/daily)
- title(can be empty string)
- notes(can be empty string)
- duedate(can be empty string, otherwise formatted datetime string of ONE FORMAT)

"createsubtask":
creates a new subtask inside a project/daily task. Args required:
- id(id of the task to create subtask for)
- title(can be empty string)

"completetask":
completes a task(any task, found by id)
- id(id of the task to complete)

"changedate"
changes the date on a task(any task, found by id)
- id(id of the task to change)
- newdate(date strings are currently just strings lol)

"changetitle"
changes the title of a task(any task, by id)
- id(id of the task to change)
- newtitle(new title)

"deletetask"
deletes a task of any kind by id
- id(id of the task to delete)

"view"
views a project/daily task by id
- id(id of the thing to view)

### Fetching(get request)

"/alldata/[taskid]"

Returns all data for a task, searching by id. Returns a json with information
(we don't know what fields will be in this json yet ngl)

"/basicdata/[taskid]"

Returns basic data for a task, searching by id. Returns a json with information
(we don't know what fields will be in this yet ngl)

"/fetchall"

Returns a list of sorted tasks. Maps "project" to a list of ids of all project tasks,
sorted in some order. Maps "daily" to a list of ids of all daily tasks sorted in some order
(sorting algorithm can be easily modified so its ok)