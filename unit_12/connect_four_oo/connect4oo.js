/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */

const game_player_div = document.querySelector("#game_player")
const player_h3 = document.createElement("h3")


class Game{

  constructor(player1_color, player2_color, WIDTH = 7, HEIGHT = 6){
    this.player1_color = player1_color;
    this.player2_color = player2_color;
    this.WIDTH = WIDTH;
    this.HEIGHT = HEIGHT;
    this.start_again = false;
    this.currPlayer = player1_color; // active player: 1 or 2
    this.board = []; // array of rows, each row is array of cells  (board[y][x])
    this.is_board_full = false;
    this.is_column_full = false;
    this.makeBoard();
    this.makeHtmlBoard();
  }

  makeBoard() {
    // TODO: set "board" to empty HEIGHT x WIDTH matrix array
    for(let y=0;y<this.HEIGHT;y++){
      this.board[y] = []
      for (let x=0;x<this.WIDTH ;x++){
          this.board[y].push(null);
        }
      }
        console.log(board);
  }

  makeHtmlBoard() {
      // TODO: get "htmlBoard" variable from the item in HTML w/ID of "board"
    game_player_div.classList.add("currentplayer")
    game_player_div.style.color = this.currPlayer.color;
    player_h3.innerText = `Player ${this.currPlayer.color} starts the game!`
    game_player_div.appendChild(player_h3)
    const htmlBoard = document.getElementById("board")
    // TODO: add comment for this code
    const top = document.createElement("tr");
    top.setAttribute("id", "column-top");
    // we binded "this(i.e. class game)" so that everytime handleclick is called, it references to itself within class Game
    top.addEventListener("click", this.handleClick.bind(this));
    console.log(this.handleClick)
    console.log(this.handleClick.bind(this))
    for (let x = 0; x < this.WIDTH; x++) {
      const headCell = document.createElement("td");
      headCell.setAttribute("id", x);
      top.append(headCell);
    }
    htmlBoard.append(top);
    // TODO: add comment for this code
    for (let y = 0; y < this.HEIGHT; y++) {
      const row = document.createElement("tr");
      for (let x = 0; x < this.WIDTH; x++) {
        const cell = document.createElement("td");
        cell.setAttribute("id", `${y}-${x}`);
        row.append(cell);
      }
      htmlBoard.append(row);
    }
  }
  
  show_player(currPlayer){
    game_player_div.innerText = ""
    game_player_div.classList.add("currentplayer")
    game_player_div.style.color = currPlayer.color;
    player_h3.innerText = `Player ${currPlayer.color}'s turn!`
    game_player_div.appendChild(player_h3)

  }
    /** findSpotForCol: given column x, return top empty y (null if filled) */
    // y - row, x - column
    findSpotForCol(x) {
      for (let y = this.HEIGHT - 1; y >= 0; y--) {
        if (!this.board[y][x]) {
          return y;
        }
      }
      return null;
    }
  
  placeInTable(y, x) {
    // TODO: make a div and insert into correct table cell
    const target_cell = document.getElementById(`${y}-${x}`);
    let colored_div = document.createElement("div")
    colored_div.classList.add("piece")
    colored_div.style.backgroundColor = this.currPlayer.color;
    target_cell.append(colored_div);
    console.log(colored_div);
    console.log(board)
  }
    
    /** endGame: announce game end */
    
  endGame(msg) {
    confirm(msg)
    if(confirm("Would you like to play again?")){
      location.reload();
    }
    return
    // TODO: pop up alert message
  }
    
    /** handleClick: handle click of column top to play piece */
    
  handleClick(evt) {
    // get x from ID of clicked cell
    let x = +evt.target.id;
    console.log(x)
    // get next spot in column (if none, ignore click)
    const y = this.findSpotForCol(x);
    if (y === null) {
      return;
    }

    // place piece in board and add to HTML table
    // TODO: add line to update in-memory board
    this.board[y][x] = this.currPlayer;
    this.placeInTable(y, x);
    
    // check for win
    if (this.checkForWin()) {
      return this.endGame(`Player ${this.currPlayer.color} won!`);
    }
    // check for tie
    // TODO: check if all cells in board are filled; if so call, call endGame
    for(let y=0;y<this.HEIGHT;y++){
      let row_check = this.board[y].every((val) => {return val !== null })
      console.log(row_check)
      if(row_check){
        this.is_board_full = true;
        continue;
      }
      else{
        this.is_board_full = false;
        break;
      }
    }
    if(this.is_board_full === true){
      this.endGame("THE GAME IS TIED!");
    }
    // switch players
    // TODO: switch currPlayer 1 <-> 2
    this.currPlayer = this.currPlayer === this.player1_color ? this.player2_color: this.player1_color;
    this.show_player(this.currPlayer)
    console.log(`current player is ${this.currPlayer}`)
  }
    
    /** checkForWin: check board cell-by-cell for "does a win start here?" */
  checkForWin() {

    const _win = cells =>
    cells.every(
      ([y, x]) =>
        y >= 0 &&
        y < this.HEIGHT &&
        x >= 0 &&
        x < this.WIDTH &&
        this.board[y][x] === this.currPlayer
    );
    // TODO: read and understand this code. Add comments to help you.
    for (var y = 0; y < this.HEIGHT; y++) {
      for (var x = 0; x < this.WIDTH; x++) {
        var horiz = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]];
        var vert = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]];
        var diagDR = [[y, x], [y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3]];
        var diagDL = [[y, x], [y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3]];
  
        if (_win(horiz) || _win(vert) || _win(diagDR) || _win(diagDL)) {
          return true;
        }
      }
    }
  }


}

class Player{
  constructor(player_color){
    this.color = player_color
  }
}


function randomRGB() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r},${g},${b})`
}
const letters = document.querySelectorAll('.letter');
const intervalId = setInterval(function () {
  for (let letter of letters) {
    letter.style.color = randomRGB();
  }
}, 1000);

/** makeBoard: create in-JS board structure:
 *    board = array of rows, each row is array of cells  (board[y][x])
 */
/** makeHtmlBoard: make HTML table and row of column tops. */
/** placeInTable: update DOM to place piece into HTML table of board */
const start_game_btn = document.querySelector('#start_game')
start_game_btn.addEventListener('click',function(){
  
  if(document.querySelector('#p1_color').value && document.querySelector('#p1_color').value)
  {
  let player1_color = new Player(document.querySelector('#p1_color').value)
  let player2_color = new Player(document.querySelector('#p2_color').value)
  new Game(player1_color, player2_color);
  }
  else{
    confirm("No colors were entered, please try again!");
    location.reload();
  }

});


document.querySelector('#reset_game').addEventListener('click',function(){
  location.reload();
})





