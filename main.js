const button = document.getElementById("completed");
const completed = document.getElementsByClassName("completed")
/*
button.addEventListener("click", () => {
    completed.classList.toggle("completed");
});
*/
const links = document.querySelectorAll(".toggle-link");

//console.log(links);

links.forEach(link => {
    link.addEventListener("click", () => {
        console.log(link.dataset.id);
    });
});