function randomRGB() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r},${g},${b})`
  }
  const letters = document.querySelectorAll('.letter');
  const intervalId = setInterval(function () {
    for (let letter of letters) {
      letter.style.color = randomRGB();
    }
  }, 1000);

  




function check_inputs(){
  const inputs = document.querySelectorAll('input');
  for(i of inputs){
    if (i.value === null){
      continue
    }
    else{
      window.alert(`${i.id} cannot be empty, please input ${i.id}`)
    }
  }
}

$('#madlib_btn').on("click",check_inputs);