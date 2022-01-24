
const guess_input_box = document.querySelector("#guess")
const guess_submit_btn = document.querySelector("#submit_guess")
const user_banner_p = document.querySelector("#user_banner")
const game_updates_p = document.querySelector("#game_updates")
BASE_URL = "http://127.0.0.1:5000/boggleapi"


guess_submit_btn.addEventListener('click', function(e){
    e.preventDefault();
    process_guess();
})

async function process_guess() {
    const guess_value = guess_input_box.value
    let res = await axios.get(BASE_URL,{params: { guess: guess_value }})
    let response_obj = res.data
    console.log(res)
    console.log(response_obj)
    show_result(response_obj)

}

function show_result(response_obj){
    let uname = response_obj['username'].toUpperCase();
    if(response_obj['is_duplicate']){
        return
    }
    if (response_obj['result'] === 'ok')
    {
        console.log(game_updates_p)
        game_updates_p.innerText = "Yay!! You guessed a word that is valid and on board!!"
        user_banner_p.innerText = `USER: ${uname}  |  SCORE: ${response_obj['score']}`
        console.log(game_updates_p)
    }
    else if (response_obj['result'] === 'not-on-board')
    {
        console.log(game_updates_p)
        game_updates_p.innerText = "Owww!! You guessed a word that is valid but not on board!!"
        user_banner_p.innerText = `USER: ${uname}  |  SCORE: ${response_obj['score']}`
        console.log(game_updates_p)
    }
    else if (response_obj['result'] === 'not-a-word')
    {
        console.log(game_updates_p)
        game_updates_p.innerText = "Noooo!! You guessed a word that is not valid!!"
        user_banner_p.innerText = `USER: ${uname}  |  SCORE: ${response_obj['score']}`
        console.log(game_updates_p)
    }


}


async function getCategoryIds() {
    let res = await axios.get(`http://jservice.io/api/categories`,{ params:{count:100}});
    res.data.map(function(data_obj){
        category_ids.push(data_obj["id"])
    });
    console.log(category_ids)
    console.log(category_ids.length)
    let total_ids = 6;
    const shuffled_arr = category_ids.sort(function(){ return 0.5 - Math.random()});
    let selected_ids = shuffled_arr.slice(0,total_ids);
    console.log(selected_ids)

    return selected_ids;
}