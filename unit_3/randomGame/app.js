console.log("hello");

const z = function countDown(num){
   let n = num;
   console.log(n)
   for(i=n;i=0;i--){
    console.log(i)   
    if(i=0){
           console.log("Done!")
       }
       else{
           setInterval(function() {
            console.log(i)   
           }, 1000);
       }
   }
   }



