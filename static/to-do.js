// // script.js
//
// document.addEventListener("DOMContentLoaded", function () {
//     // Retrieve todos from the server on page load
//     fetch("/get_todos")
//         .then(response => response.json())
//         .then(data => {
//             data.todos.forEach(todo => {
//                 addTodoToList(todo.id, todo.text, todo.completed);
//             });
//         });
// });
//
// function addTodo() {
//     var todoText = document.getElementById("todoInput").value;
//
//     if (todoText.trim() !== "") {
//         fetch("/add_todo", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({
//                 todo_text: todoText,
//             }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 addTodoToList(data.todo.id, todoText, false);
//                 document.getElementById("todoInput").value = "";
//             } else {
//                 console.error("Failed to add todo:", data.error);
//             }
//         });
//     }
// }
//
// function addTodoToList(todoId, todoText, completed) {
//     var li = document.createElement("li");
//
//     var checkbox = document.createElement("input");
//     checkbox.type = "checkbox";
//     checkbox.checked = completed;
//
//     var label = document.createElement("label");
//     label.appendChild(document.createTextNode(todoText));
//
//     li.appendChild(checkbox);
//     li.appendChild(label);
//
//     document.getElementById("todoList").appendChild(li);
// }
//
// function deleteAllTodos() {
//     fetch("/delete_all_todos", {
//         method: "DELETE",
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             clearTodoList();
//         } else {
//             console.error("Failed to delete all todos:", data.error);
//         }
//     });
// }
//
// function clearTodoList() {
//     var todoList = document.getElementById("todoList");
//     while (todoList.firstChild) {
//         todoList.removeChild(todoList.firstChild);
//     }
// }

// to-do.js

document.addEventListener("DOMContentLoaded", function () {
    // Retrieve todos from the server on page load
    fetch("/get_todos_pink")
        .then(response => response.json())
        .then(data => {
            data.todos.forEach(todo => {
                if (todo.container === "pink") {
                    addTodoToList(todo.id, todo.text, todo.completed, "todoListPink");
                }
            });
        });
    fetch("/get_todos_blue")
        .then(response => response.json())
        .then(data => {
            data.todos.forEach(todo => {
                if (todo.container === "blue") {
                    addTodoToList(todo.id, todo.text, todo.completed, "todoListBlue");
                }
            });
        });
});



function addTodoPink() {
    var todoText = document.getElementById("todoInputPink").value;

    if (todoText.trim() !== "") {
        fetch("/add_todo_pink", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                todo_text: todoText,
                container: "pink",
                completed: false
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                addTodoToList(data.todo.id, todoText, false, "todoListPink");
                document.getElementById("todoInputPink").value = "";
            } else {
                console.error("Failed to add todo:", data.error);
            }
        })
        .catch(error => {
            console.error("Error in addTodoPink:", error);
        });
    }
}
//
// function addTodoBlue() {
//     var todoText = document.getElementById("todoInputBlue").value;
//
//     if (todoText.trim() !== "") {
//         fetch("/add_todo_blue", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({
//                 todo_text: todoText,
//                 container: "blue",
//             }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 addTodoToList(data.todo.id, todoText, false, "todoListBlue");
//                 document.getElementById("todoInputBlue").value = "";
//             } else {
//                 console.error("Failed to add todo:", data.error);
//             }
//         })
//         .catch(error => {
//             console.error("Error in addTodoBlue:", error);
//         });
//     }
// }

function addTodoBlue() {
    var todoText = document.getElementById("todoInputBlue").value;

    if (todoText.trim() !== "") {
        fetch("/add_todo_blue", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                todo_text: todoText,
                container: "blue",
                completed: false, // Initialize as unchecked
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                addTodoToList(data.todo.id, todoText, false, "todoListBlue");
                document.getElementById("todoInputBlue").value = "";
            } else {
                console.error("Failed to add todo:", data.error);
            }
        })
        .catch(error => {
            console.error("Error in addTodoBlue:", error);
        });
    }
}

function deleteAllTodosPink() {
    fetch("/delete_all_todos_pink", {
        method: "DELETE",
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            clearTodoList("todoListPink");
        } else {
            console.error("Failed to delete all todos (Pink):", data.error);
        }
    });
}

function deleteAllTodosBlue() {
    fetch("/delete_all_todos_blue", {
        method: "DELETE",
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            clearTodoList("todoListBlue");
        } else {
            console.error("Failed to delete all todos (Blue):", data.error);
        }
    });
}

function clearTodoList(listId) {
    var todoList = document.getElementById(listId);
    while (todoList.firstChild) {
        todoList.removeChild(todoList.firstChild);
    }
}

// function addTodoToList(todoId, todoText, completed, listId) {
//     var li = document.createElement("li");
//
//     var checkbox = document.createElement("input");
//     checkbox.type = "checkbox";
//     checkbox.checked = completed;
//
//     var label = document.createElement("label");
//     label.appendChild(document.createTextNode(todoText));
//
//     li.appendChild(checkbox);
//     li.appendChild(label);
//
//     document.getElementById(listId).appendChild(li);
// }

function addTodoToList(todoId, todoText, completed, listId) {
    var li = document.createElement("li");

    var checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = completed;

    checkbox.addEventListener("change", function() {
        updateTodoStatus(todoId, checkbox.checked);
    });

    li.appendChild(checkbox);

    var label = document.createElement("label");
    label.appendChild(document.createTextNode(todoText));
    li.appendChild(label);

    document.getElementById(listId).appendChild(li);
}

function updateTodoStatus(todoId, completed) {
    fetch("/update_todo", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            todo_id: todoId,
            completed: completed,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            console.error("Failed to update todo status:", data.error);
        }
    })
    .catch(error => {
        console.error("Error updating todo status:", error);
    });
}

