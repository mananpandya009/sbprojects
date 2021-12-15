



$("#add_rating_btn").on('click', function (e){
    e.preventDefault();
    let title = $('input').eq(0).val();
  let rating = $('input').eq(1).val();
    let output = process_ratings(title, rating)

    $('ul').append(output)
  });
  
 function process_ratings(title, rating){
    return `
    <li>
    <span><p>Title: ${title} has ratings: ${rating}  <button id="remove_rating">Remove</button></p></span>
    </li>
    `
 }

 $("ul").on('click',function(e){
    e.target.parentNode.parentNode.parentNode.remove();
 })