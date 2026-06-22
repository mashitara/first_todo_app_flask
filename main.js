const button = document.getElementById("completed");
const completed = document.getElementsByClassName("completed")
/*
button.addEventListener("click", () => {
    completed.classList.toggle("completed");
});
*/

//イベント委譲
document.querySelector(".task-item")
.addEventListener("click", async function(e) {
    e.preventDefault();
    if (e.target.classList.contains("toggle-link")) {
        
        console.log(e.target.dataset.id);
        
        const response = await fetch(`/toggle/${e.target.dataset.id}`,{
            method: "POST"
        });
        
        console.log(e.target.parentElement);
        const li = e.target.parentElement;
        const span = li.querySelector("span");

        //const span2 = document.querySelector(".completed");
        span.classList.toggle("completed");

        const data = await response.json();
        console.log(data);

    } else if (e.target.classList.contains("delete-btn")) {
        fetch(`/delete/${e.target.dataset.id}`, {
            method: "POST"
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.success) {
                document.querySelector(`#task-${e.target.dataset.id}`).remove();
            }
        });
    } else if (e.target.classList.contains("edit-btn")) {
        if (e.target.textContent === "編集") {
                
            const li = e.target.parentElement;
            const span = li.querySelector("span");

            const title = span.textContent;
            span.outerHTML = `<input class="edit-input" value="${title}">`;
            e.target.textContent = "保存";
        } else {
            
            const li = e.target.parentElement;
            const input = li.querySelector(".edit-input")
            const title = input.value;
            const formData = new FormData();
            formData.append("title", title);

            fetch(`/edit/${e.target.dataset.id}`, {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.success) {
                    input.outerHTML = `<span>${title}</span>`
                    e.target.textContent = "編集"
                }
            });
        }
    }
});

//完了したタスクに線を引くよを非同期化
/*
const links = document.querySelectorAll(".toggle-link");
links.forEach(link => {
    link.addEventListener("click", async (event) => {
        event.preventDefault();

        //console.log(link.dataset.id);
        //console.log(link);
        //console.log(link.parentElement);
        const response = await fetch(`/toggle/${link.dataset.id}`,{
            method: "POST"
        });
        const span = link.parentElement.querySelector("span");
        span.classList.toggle("completed");

        const data = await response.json();
        //console.log(data);

    });
});
*/

/*
//削除ボタンを非同期化
document.querySelectorAll(".delete-btn")
.forEach(button => {
    button.addEventListener("click", function (event) {
        event.preventDefault();
        fetch(`/delete/${this.dataset.id}`, {
            method: "POST"
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.success) {
                document.querySelector(`#task-${this.dataset.id}`).remove();
            }
        });
    });
});
*/

//タスク追加処理を非同期化

document.querySelector(".add-btn")
.addEventListener("click", function (e) {
    e.preventDefault();

    const input = document.querySelector("[name ='title']");
    const title = input.value.trim();

    if (title === "") {
        alert("タスクを入力してください");
        return;
    }
    
    const form = document.querySelector(".form");
    const formData = new FormData(form);

    fetch(`/add`, {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            alert(data.message);
            return;
        }
        const taskList = document.querySelector(".task-item")
        taskList.insertAdjacentHTML(
            "afterbegin",
            `<li id="task-${data.id}">
                <span>${data.title}</span>
                <button class="edit-btn" data-id="${data.id}">編集</button>
                <button class="toggle-link" data-id="${data.id}">完了</button>
                <button class="delete-btn" data-id="${data.id}">削除</button>
            </li>
            `
        );
    });
});