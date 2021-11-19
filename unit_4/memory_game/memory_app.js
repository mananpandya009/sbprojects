localStorage.clear();
const gameContainer = document.getElementById("game");
var div_identifier = ""
var div_color = ""
let card1_isclicked = false;
let card2_isclicked = false;
let card_1 = null;
let card1_color = "";
let card_2 = null;
let card2_color = "";
let card_clicked = null;
let cards_matched = 0;

const COLORS = [
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "red",
  "blue",
  "green",
  "orange",
  "purple",
];

// here is a helper function to shuffle an array
// it returns the same array with values shuffled
// it is based on an algorithm called Fisher Yates if you want ot research more
function shuffle(array) {
  let counter = array.length;

  // While there are elements in the array
  while (counter > 0) {
    // Pick a random index
    let index = Math.floor(Math.random() * counter);

    // Decrease counter by 1
    counter--;

    // And swap the last element with it
    let temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }

  return array;
}

let shuffledColors = shuffle(COLORS);
// this function loops over the array of colors
// it creates a new div and gives it a class with the value of the color
// it also adds an event listener for a click for each card
function createDivsForColors(colorArray) {

    
    for (let color of colorArray) {
    // create a new div
    const newDiv = document.createElement("div");
    
    // newDiv.setAttribute("onmouseup","countclicks()")
    // give it a class attribute for the value we are looping over
    newDiv.classList.add(color);
    
    
    // call a function handleCardClick when a div is clicked on
    
    newDiv.addEventListener("click", handleCardClick);

    // append the div to the element with an id of game
    gameContainer.append(newDiv);
  }
}


function handleCardClick(e){


    if(e.target.classList.contains("clicked")){
        console.log("already clicked, returning")
    }

    card_clicked = e.target;
    card_clicked.style.background = card_clicked.classList[0];
    if(card_1 === null || card_2 === null){

        if(card_1 === null && !card1_isclicked ){
            card_1 = card_clicked;
            card1_color = card_clicked.classList[0];
            card_clicked.classList.add("clicked");
            console.log(card_clicked.classList);
            console.log("card 1 is this,",card1_color);
            card1_isclicked = true;
            
        }

        else if(card_2 == null && card1_isclicked === true)
        {
            card_2 = card_clicked;
            card2_color = card_clicked.classList[0];
            card_clicked.classList.add("clicked");
            console.log(card_clicked.classList);
            console.log("card 2 is this,",card2_color);
            card2_isclicked = true;
        }
        else{
            console.log("more than 2 cards clicked")
        }
    }

    if(card1_color && card2_color){
        if(card1_color === card2_color){
            console.log("cards have matched");
            card_1.removeEventListener("click","click", handleCardClick(e));
            card_2.removeEventListener("click", "click", handleCardClick(e));
            card_1 = null;
            card_2 = null;


        }
        else{
            setTimeout(function(){
            card_1.style.background = ""
            card_2.style.background = ""
            card_1.classList.remove("clicked");
            card_2.classList.remove("clicked");
            card1_isclicked = false;
            card2_isclicked = false;
            card_1 = null;
            card1_color = "";
            card_2 = null;
            card2_color = "";
            },1000);
        }
    }
    

        
    
    
}


createDivsForColors(shuffledColors);

