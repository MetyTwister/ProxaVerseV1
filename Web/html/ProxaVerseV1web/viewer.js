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

const viewer = document.getElementById('viewer');
const loader = document.getElementById('loader');

viewer.addEventListener('load', () => {
    loader.style.opacity = 0;
    setTimeout(() => loader.style.display = 'none', 1500); //higher timeout = longer loader animation
});