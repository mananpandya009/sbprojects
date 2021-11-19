

function countDown(num){
    var n = num
    
var count = setInterval(function(){
    console.log(n);
    n--
    if(n === 0){
        console.log("Done!!!")
        clearInterval(count);
    }
},1000)        
           }


function randomGame(){

var random_number_counter = 0;
var compare_random_value = setInterval(function(){
    random_number = Math.random() * 1;
    
    random_number_counter++
    if(random_number > 0.75){
        console.log("The number of tries it took before we found a number greater than .75 is:",random_number_counter)
        clearInterval(compare_random_value);
    
    }
},1000)

}