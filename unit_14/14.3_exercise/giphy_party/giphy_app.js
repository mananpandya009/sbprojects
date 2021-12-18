const search_input_box = document.getElementById('search_text');
let gif_url = "";
let gif_res;
let gif_number = 0;
const gif_submit_btn = document.querySelector('#gif_submit_btn');
const gif_result_container = document.querySelector('#gif_container');



gif_submit_btn.addEventListener('click',function(){
    
    search_text = search_input_box.value;
    console.log(search_text)
    gif_url,gif_res = get_gif(search_text)
    console.log(gif_res)
    console.log(gif_url)
    

});


async function get_gif(search_text) {
    let gif_object = document.createElement('img');
    const api_key = "kEgJZ3xAM4xsjjBDtKM2uAsEyOZmX1Kv"
    const q= search_text
    let res = await axios.get(`http://api.giphy.com/v1/gifs/search`, { params: { q,api_key } });
    let gif_url = res.data.data[gif_number]["images"]["original"]["url"]
    console.log(res)
    console.log(res.data.data[gif_number]["images"]["original"]["url"])
    gif_number++;

    gif_object.src = gif_url;
    gif_object.addEventListener('load', function(e){
        e.preventDefault();
        process_gif(gif_object);
        console.log(gif_object)
        
    });
    return gif_url, res;
  }


function process_gif(gif_object){
    let gif_result_div = document.createElement('div')
    gif_result_div.classList.add('gif_result_subdiv')

    let remove_gif_btn = document.createElement('button')
    remove_gif_btn.id = "remove_gif";
    remove_gif_btn.innerText = "X";

    console.log(`Gif was loaded from ${gif_url}`);

    gif_result_div.appendChild(gif_object);
    gif_result_div.appendChild(remove_gif_btn);
    gif_result_container.appendChild(gif_result_div);
    search_input_box.innerText = "";
    let remove_buttons = document.querySelectorAll('#remove_gif');
    console.log(remove_buttons);
    for (btn of remove_buttons){
    
    btn.addEventListener('click',function(e){
        console.log(e.target)
        e.target.parentElement.remove();
    });
}
}

