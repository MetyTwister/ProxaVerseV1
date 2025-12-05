//
//
// Crazy word effect
//
//
const letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let interval = null;

document.getElementById("PVeffect").onmouseover = event => {
    let iteration = 0;

    clearInterval(interval);

    interval = setInterval(() => {

        event.target.innerText = event.target.innerText
            .split("") 
            .map((letter, index) => {
                if (index < iteration) {
                    return event.target.dataset.value[index];
                }

                return letters[Math.floor(Math.random() * 26)]
            })
            .join("");

    if(iteration >= event.target.dataset.value.length){
        clearInterval(interval);
    } 

    iteration += 1 / 2;
    }, 30);
}

//
//
// Crazy word effect
//
//

const dialog1 = document.getElementById("dialog1")
const dialog2 = document.getElementById("dialog2")

const openTile1 = () => {
    dialog1.showModal();
    document.body.classList.add("no-scroll");
}

const openTile2 = () => {
    dialog2.showModal();
    document.body.classList.add("no-scroll");
}

dialog1.addEventListener("click", e => {
    const dialogDimensions1 = dialog1.getBoundingClientRect()
    if (
        e.clientX < dialogDimensions1.left ||
        e.clientX > dialogDimensions1.right ||
        e.clientY < dialogDimensions1.top ||
        e.clientY > dialogDimensions1.bottom
    ) {
        dialog1.close();
        document.body.classList.remove("no-scroll");
    }
})

dialog2.addEventListener("click", e => {
    const dialogDimensions2 = dialog2.getBoundingClientRect()
    if (
        e.clientX < dialogDimensions2.left ||
        e.clientX > dialogDimensions2.right ||
        e.clientY < dialogDimensions2.top ||
        e.clientY > dialogDimensions2.bottom
    ) {
        dialog2.close();
        document.body.classList.remove("no-scroll");
    }
})
