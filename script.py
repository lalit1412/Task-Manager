# import PyScript's Element API
from pyscript import Element
from pyodide.ffi import create_proxy


# dictionary to store all tasks
allTasks = {}

# create a reference to the h1 element
heading = Element("heading")

# styling for heading
heading.element.style.backgroundColor = "#7765E3"
heading.element.style.color = "#ffffff"
heading.element.style.textAlign = "center"
heading.element.style.margin = "0px"
heading.element.style.padding = "10px"
heading.element.style.fontSize = "26px"

# styling for the body element
mainBody = Element("main")
mainBody.element.style.backgroundColor = "#232C33"
mainBody.element.style.margin = "0px"
mainBody.element.style.fontFamily = "Monospace"

# create a reference to the container
container = Element("container")

# styling for the container
container.element.style.width = "460px"
container.element.style.margin = "20px auto"

# select the input field
inputField = container.select("input")

# styling  for input field
inputField.element.style.padding = "7px"
inputField.element.style.width = "70%"
inputField.element.style.border = "none"
inputField.element.style.borderRadius = "5px"
inputField.element.style.marginRight = "5px"

# select the button
addBtn = container.select("button")

# styling the button
addBtn.element.style.backgroundColor = "#28C2FF"
addBtn.element.style.color = "#ffffff"
addBtn.element.style.border = "none"
addBtn.element.style.borderRadius = "5px"
addBtn.element.style.padding = "7px 15px"
addBtn.element.style.cursor = "pointer"


# create a reference to the tasksList
tasksList = Element("tasksList")

# create a reference to the template
taskTemplate = Element("taskTemplate")

# select the li element
taskListTemplate = taskTemplate.select("li", from_content=True)


# function called when button is clicked
def onAddBtnClick(event):
    #print("Clicked!")
    # store value entered into input field
    task = inputField.element.value
    #print(task)
    
    # dictionary to store task name and status
    newTask = {
        "name": task,
        "status": "Not started"
    }
    
    # add newTask dictionary to allTasks dictionary
    allTasks[task] = newTask
    #print(allTasks)
    
    # clear text field after task submission
    inputField.element.value = ""
    
    # call showAllTasks()
    showAllTasks()

    
# function to display all existing tasks
def showAllTasks():
    #print(allTasks)
    
    # clear previous ul element 
    tasksList.element.innerHTML = ""
    
    # iterate over all submitted tasks
    # all tasks are stored to allTasks dictionary
    for i in allTasks:
        #print(allTasks[i])
        
        # clone the li element
        newTaskList = taskListTemplate.clone()
        
        # styling for new task list
        newTaskList.element.style.listStyleType = "none"
        newTaskList.element.style.marginBottom = "10px"
        newTaskList.element.style.marginLeft = "-20px"
        
        # display the task name
        taskName = newTaskList.select("span")
        taskName.element.textContent = allTasks[i]["name"]
        
        # styling for task name span
        taskName.element.style.color = "#ffffff"
        taskName.element.style.fontSize = "16px"
        
        # select the button
        tagBtn = newTaskList.select("button")
        tagBtn.element.textContent = allTasks[i]["status"]
        
        # styling for task status button
        # change background color of the button depending on the task status
        if (allTasks[i]["status"] == "Not started"):
            tagBtn.element.style.backgroundColor = "#FF5A5F"
        else:
            tagBtn.element.style.backgroundColor = "#02C39A"
        tagBtn.element.style.color = "#ffffff"
        tagBtn.element.style.fontSize = "16px"
        tagBtn.element.style.width = "150px"
        tagBtn.element.style.display = "inline-block"
        tagBtn.element.style.textAlign = "center"
        tagBtn.element.style.padding = "5px"
        tagBtn.element.style.border = "none"
        tagBtn.element.style.borderRadius = "5px"
        tagBtn.element.style.cursor = "pointer"
        
        # add "click" event to task status button
        tagBtn.element.addEventListener("click", create_proxy(toggleStatus))
        
        # append the new task to the list
        tasksList.element.appendChild(newTaskList.element)



# function called when task status button is clicked
def toggleStatus(event):
    #print(event.currentTarget)
    
    # access the li (parent element) of clicked button
    parent = event.currentTarget.parentElement
    
    # access task name span 
    # task name span is second child node of the li
    key = parent.children[1].textContent
    #print(key)
    
    # if current status is set to "Not started", change to "Done" when clicked
    if (allTasks[key]["status"] == "Not started"):
        allTasks[key]["status"] = "Done"
    
    # else if current status is set to "Done", change to "Not started" when clicked
    else:
        allTasks[key]["status"] = "Not started"

    # showAllTasks() to toggle status
    showAllTasks()
    
    
# add "click" event to button 
# onAddBtnClick function is called
addBtn.element.addEventListener("click", create_proxy(onAddBtnClick) )
    



