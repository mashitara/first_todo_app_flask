const button = document.getElementById("completed");
const completed = document.getElementsByClassName("completed")
/*
button.addEventListener("click", () => {
    completed.classList.toggle("completed");
});
*/

//完了したタスクに線を引くよを非同期化
const links = document.querySelectorAll(".toggle-link");
links.forEach(link => {
    link.addEventListener("click", async (event) => {
        event.preventDefault();

        //console.log(link.dataset.id);
        console.log(link);
        console.log(link.parentElement);
        const response = await fetch(`/toggle/${link.dataset.id}`,{
            method: "POST"
        });
        const span = link.parentElement.querySelector("span");
        span.classList.toggle("completed");

        const data = await response.json();
        console.log(data);

    });
});

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