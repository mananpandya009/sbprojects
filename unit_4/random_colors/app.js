const h1 = document.querySelector('h1');

h1.style.color = randomrgb();

function randomrgb(){
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r},${g},${b})`

}



const letters = document.querySelectorAll('.letters');
setInterval(function(){
  for(let letter of letters){
    letter.style.color = randomrgb();
  }
    
},1000)