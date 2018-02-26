let i = 0;
let num = document.getElementById('num').innerHTML;
let clicked = false;
let run = null;
let vid = document.getElementById('vid')

function init() {
    i = 0;
    let frame_zero = document.getElementById(`frame0`);
    frame_zero.style.display = "block";
    i++;
}

function play() {
    let frame_curr = document.getElementById(`frame${i-1}`)
    let frame_next = document.getElementById(`frame${i}`)
    frame_curr.style.display = "none";
    frame_next.style.display = "block";
    i++;
    console.log(i);
    clearInterval(run);
    run = setInterval(play, 40+Math.random());
    if (i >= num) {
        clearInterval(run);
    }
}

window.addEventListener('click', ()=>{
    if (!clicked) {
        clicked = true;
        vid.play()
        if (i < num) {
            run = setInterval(play, 40+Math.random());
        } else {
            let frame_next = document.getElementById(`frame${num-1}`)
            frame_next.style.display = "none";
            init();
        }
    } else {
        clicked = false;
        clearInterval(run);
        vid.pause();
        if (i >= num) {
            let frame_next = document.getElementById(`frame${num-1}`)
            frame_next.style.display = "none";
            init();
        }
    }
})

init();