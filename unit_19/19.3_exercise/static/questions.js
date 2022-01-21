
function check_user_input()
{
  const choice1 = document.querySelector("#choice1")
  const choice2 = document.querySelector("#choice2")

  if(choice1.checked === true && choice2.checked === true)
  {
      console.log("whaaaaaat!")
    return
  }

}




document.querySelector("#submit_answer_btn").addEventListener("click",check_user_input);