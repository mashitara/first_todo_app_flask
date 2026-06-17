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