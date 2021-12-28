"use strict";

/******************************************************************************
 * Handling navbar clicks and updating navbar
 */

/** Show main list of all stories when click site name */

function navAllStories(evt) {
  console.debug("navAllStories", evt);
  hidePageComponents();
  putStoriesOnPage();
}

$body.on("click", "#nav-all", navAllStories);

/** Show login/signup on click on "login" */

function navLoginClick(evt) {
  console.debug("navLoginClick", evt);
  hidePageComponents();
  $loginForm.show();
  $signupForm.show();
}

$navLogin.on("click", navLoginClick);

/** When a user first logins in, update the navbar to reflect that. */

function updateNavOnLogin() {
  console.debug("updateNavOnLogin");
  $(".main-nav-links").show();
  $navLogin.hide();
  $loginForm.hide();
  $signupForm.hide();
  $navLogOut.show();
  $navAddStory.show();
  $navOwnStory.show();
  $navFvrtStories.show();
 
  $navUserProfile.text(`${currentUser.username}`).show();
}
let form_toggler = 0;

function show_add_story_form() {
  console.debug("show_add_story_form");
  if(form_toggler % 2 === 0){
  $(".main-nav-links").show();
  $addstoryForm.show();
  form_toggler++;}
  else{
    $(".main-nav-links").show();
  $addstoryForm.hide();
  form_toggler++;
  }
 }

$navAddStory.on("click",show_add_story_form)





