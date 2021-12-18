/** Given a query string, return array of matching shows:
 *     { id, name, summary, episodesUrl }
 */


/** Search Shows
 *    - given a search term, search for tv shows that
 *      match that query.  The function is async show it
 *       will be returning a promise.
 *
 *   - Returns an array of objects. Each object should include
 *     following show information:
 *    {
        id: <show id>,
        name: <show name>,
        summary: <show summary>,
        image: <an image from the show data, or a default imege if no image exists, (image isn't needed until later)>
      }
 */
async function searchShows(query) {
  // TODO: Make an ajax request to the searchShows api.  Remove
  // hard coded data.
  let q = query
  let res = await axios.get(`http://api.tvmaze.com/search/shows`, { params: { q } });
  let show_obj = {}
  let shows = []
  console.log(res)
  console.log(res.data[0]["show"]["id"]);
  console.log(res.data[0]["show"]["name"]);
  console.log(res.data[0]["show"]["summary"]);
  console.log(res.data[0]["show"]["image"]["original"]);

  for(let i=0;i<res.data.length;i++){
    console.log(res.data[i])
    show_obj["id"] = res.data[i]["show"]["id"];
    show_obj["name"] = res.data[i]["show"]["name"];
    show_obj["summary"] = res.data[i]["show"]["summary"];
    if(res.data[i]["show"]["image"]){
    show_obj["image"] = res.data[i]["show"]["image"]["original"]}
    else{
      show_obj["image"] = "https://store-images.s-microsoft.com/image/apps.65316.13510798887490672.6e1ebb25-96c8-4504-b714-1f7cbca3c5ad.f9514a23-1eb8-4916-a18e-99b1a9817d15?mode=scale&q=90&h=300&w=300"
    }
    console.log(show_obj)
    shows.push(show_obj)
    show_obj = {}
    console.log(shows)

  }
  return shows;
}



/** Populate shows list:
 *     - given list of shows, add shows to DOM
 */

function populateShows(shows) {
  const $showsList = $("#shows-list");
  $showsList.empty();

  for (let show of shows) {
    
    let $item = $(
      `<div class="col-md-6 col-lg-3 Show" data-show-id="${show.id}">
         <div class="card" data-show-id="${show.id}">
         <img class="card-img-top" src="${show.image}">  
         <div class="card-body">
             <h5 class="card-title">${show.name}</h5>
             <p class="card-text">${show.summary}</p>
           </div>
          <button id ="episodes_btn"> Show Episodes</button>
         </div>
       </div>
      `);

    $showsList.append($item);
  }
}


function populateEpisodes(episodes) {
  const $ep_List = $("#episodes-list");
  $ep_List.empty();

  for (let ep of episodes) {
   
    let $item = $(
      `<li>
      ${ep.name}
      (season ${ep.season}, episode ${ep.number})
        </li>
      `);

    $ep_List.append($item);
  }
  $("#episodes-area").show();
}

$("#shows-list").on("click",async function load_episodes(evt){
  evt.preventDefault();
  let show_id = $(evt.target).closest(".Show").data("show-id");
  console.log(show_id);
  let episodes = await getEpisodes(show_id)
  populateEpisodes(episodes);  
});



/** Handle search form submission:
 *    - hide episodes area
 *    - get list of matching shows and show in shows list
 */

$("#search-form").on("submit", async function handleSearch (evt) {
  evt.preventDefault();

  let query = $("#search-query").val();
  if (!query) return;

  $("#episodes-area").hide();

  let shows = await searchShows(query);
  populateShows(shows);
});


/** Given a show ID, return list of episodes:
 *      { id, name, season, number }
 */

async function getEpisodes(id) {
  // TODO: get episodes from tvmaze
  //       you can get this by making GET request to
  //       http://api.tvmaze.com/shows/SHOW-ID-HERE/episodes
  
  let res = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`);
  console.log(res)
  let episodes_obj = {}
  let episodes = []
  console.log(res)
  console.log(res.data[0]["id"]);
  console.log(res.data[0]["name"]);
  console.log(res.data[0]["season"]);
  console.log(res.data[0]["number"]);

  for(let i=0;i<res.data.length;i++){
    console.log(res.data[i])
    episodes_obj["id"] = res.data[i]["id"];
    episodes_obj["name"] = res.data[i]["name"];
    episodes_obj["season"] = res.data[i]["season"];
    episodes_obj["number"] = res.data[i]["number"];
    console.log(episodes_obj)
    episodes.push(episodes_obj)
    episodes_obj = {}
    console.log(episodes)

  }

  return episodes;
    // TODO: return array-of-episode-info, as described in docstring above
}
