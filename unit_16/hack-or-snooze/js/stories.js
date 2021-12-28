"use strict";

// This is the global list of the stories, an instance of StoryList
let storyList;
let favoriteList;

/** Get and show stories when site first loads. */

async function getAndShowStoriesOnStart() {
  storyList = await StoryList.getStories();
  $storiesLoadingMsg.remove();

  putStoriesOnPage();
}

/**
 * A render method to render HTML for an individual Story instance
 * - story: an instance of Story
 *
 * Returns the markup for the story.
 */

function generateStoryMarkup(story) {
  // console.debug("generateStoryMarkup", story);
  const hostName = story.getHostName();
  if(!currentUser){
    return $(`
      <li id="${story.storyId}">
        <i class="far fa-star favorite_stories"></i>      
        <a href="${story.url}" target="a_blank" class="story-link">
          ${story.title}
        </a>
        <small class="story-hostname">(${hostName})</small>
        <small class="story-author">by ${story.author}</small>
        <small class="story-user">posted by ${story.username}</small>
      </li>
    `);
  }

  //console.log(currentUser.favorites);
  if (currentUser.favorites.length > 0)
  {
   for(let fstory of currentUser.favorites){
      if (story.storyId === fstory.storyId){
        console.log(`favorite story found, painting the star for story id ${fstory.storyId}`);
        return $(`
          <li id="${story.storyId}">
            <i class="fas fa-star favorite_stories"></i>
            <a href="${story.url}" target="a_blank" class="story-link">
              ${story.title}
            </a>
            <small class="story-hostname">(${hostName})</small>
            <small class="story-author">by ${story.author}</small><button id="remove-btn" class="remove-story-btn"> X </button>
            <small class="story-user">posted by ${story.username}</small>
          </li>
        `);
      }}}
  
  return $(`
        <li id="${story.storyId}">
          <i class="far fa-star favorite_stories"></i>        
          <a href="${story.url}" target="a_blank" class="story-link">
            ${story.title}
          </a>
          <small class="story-hostname">(${hostName})</small>
          <small class="story-author">by ${story.author} </small><button id="remove-btn" class="remove-story-btn"> X </button>
          <small class="story-user">posted by ${story.username}</small>
        </li>
      `);
}

 

/** Gets list of stories from server, generates their HTML, and puts on page. */

function putStoriesOnPage() {
  console.debug("putStoriesOnPage");
  $allStoriesList.empty();
  // loop through all of our stories and generate HTML for them
  for (let story of storyList.stories) {
    const $story = generateStoryMarkup(story);
    $allStoriesList.append($story);
  }
  $allStoriesList.show();
}

function putFvrtStoriesOnPage() {
 
  console.debug("putFvrtStoriesOnPage");
  $allStoriesList.empty();

  // loop through all of our stories and generate HTML for them
  for (let story of currentUser.favorites) {
    const $story = generateStoryMarkup(story);
    $allStoriesList.append($story);
  }
  $allStoriesList.show();
}

$navFvrtStories.on("click",putFvrtStoriesOnPage)


function putOwnStoriesOnPage() {
  console.debug("putStoriesOnPage");
  $allStoriesList.empty();

  // loop through all of our stories and generate HTML for them
  for (let story of storyList.stories) {
      if(currentUser.username === story.username){
        const $story = generateStoryMarkup(story);
        $allStoriesList.append($story);
      }
    }
  $allStoriesList.show();
}

$navOwnStory.on("click", putOwnStoriesOnPage)



async function favorite_story(evt){
  if(!currentUser){
    return;
  }
  let token = localStorage.token;
  let clicked_story_id = evt.target.parentNode.id;
  console.log(evt.target.id)
  let username = currentUser.username;
  let clicked_star = evt.target
  //console.log(clicked_story_id)
  //console.log(Array.from(clicked_star.classList));
  if(Array.from(clicked_star.classList).includes("far")){
    for (let story of storyList.stories) {
      if(story.storyId === clicked_story_id){
        console.log(story)
        clicked_star.classList.remove("far")
        clicked_star.classList.add("fas")
        //currentUser.favorites.push(story)
        const response = await axios({
          url: `${BASE_URL}/users/${currentUser.username}/favorites/${clicked_story_id}`,
          method: "POST",
          params: { token },
        });
      break;
      }
    }
  }
  else{
    for (let story of storyList.stories) {
      if(story.storyId === clicked_story_id){
        console.log(story)
        //currentUser.favorites.splice(currentUser.favorites.indexOf(story),1)
        clicked_star.classList.remove("fas")
        clicked_star.classList.add("far")
        const response = await axios({
          url: `${BASE_URL}/users/${currentUser.username}/favorites/${clicked_story_id}`,
          method: "DELETE",
          params: { token }
        });
        //console.log(currentUser.favorites)
        break;
      }
    }
  }
}

$allStoriesList.on("click",".favorite_stories", favorite_story)



async function remove_story(evt){
  console.log(currentUser.loginToken)

  let clicked_story_id = evt.target.parentNode.id;
  console.log(evt.target.id)
  const response = await axios({
  url: `${BASE_URL}/stories/${clicked_story_id}`,
  method: "DELETE",
  data: { "token": currentUser.loginToken }
  });
  evt.target.closest('li').remove();
    

}


async function submit_story(evt) {
  console.debug("submit a story", evt);
  evt.preventDefault();
  const story_title = $("#story-title").val();
  const story_author = $("#story-author").val();
  const story_url = $("#story-url").val();
  let newStory = {
    "title" : story_title,
    "author" : story_author,
    "url" : story_url
  }
  console.log(newStory);
  let story = await StoryList.addStory(currentUser,newStory);
  const $new_story_element = generateStoryMarkup(story);
  $new_story_element.appendTo($allStoriesList)
  // User.signup retrieves user info from API and returns User instance
  // which we'll make the globally-available, logged-in user.
  $addstoryForm.trigger("reset");
}
//$('ol button').on("click", remove_story)
$addstoryForm.on("submit", submit_story);
$allStoriesList.on("click", ".remove-story-btn", remove_story)






