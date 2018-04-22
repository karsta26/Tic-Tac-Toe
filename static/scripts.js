let Game = {
    userTurn: true,
    userMark: 'X',
    boardSize: 10,
    canvasSize: 500,
    lineWidth: 1,
    fieldPadding: 7,
    marksToWin: 5,
    difficultyLevel: 'easy',
    playing: false,
    board: [],
    init: function () {
        console.log('initializing...');
        this.myCanvas = document.getElementById('my-canvas');
        this.myCanvas.width = this.canvasSize;
        this.myCanvas.height = this.canvasSize;
        this.ctx = this.myCanvas.getContext('2d');
        this.ctx.lineWidth = this.lineWidth;
        this.myCanvas.addEventListener('click', this.userMove);
        let okButton = document.getElementById('ok-button');
        okButton.onclick = this.handleForm;
        let restartButton = document.getElementById('restart-button');
        restartButton.onclick = this.handleForm;
    },
    drawBoard: function () {
        console.log('drawing board');
        this.ctx.clearRect(0, 0, this.canvasSize, this.canvasSize);
        this.ctx.strokeStyle = 'black';
        for (let i = 0; i < this.boardSize - 1; ++i) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, this.fieldSize*(i + 1) + this.lineWidth*i);
            this.ctx.lineTo(this.canvasSize, this.fieldSize*(i + 1) + this.lineWidth*i);
            this.ctx.stroke();
            this.ctx.beginPath();
            this.ctx.moveTo(this.fieldSize*(i + 1) + this.lineWidth*i, 0);
            this.ctx.lineTo(this.fieldSize*(i + 1) + this.lineWidth*i, this.canvasSize);
            this.ctx.stroke();
        }
    },
    handleForm: function () {
        let formValidated = true;
        let XMark = document.getElementById('X-mark');
        let OMark = document.getElementById('O-mark');
        if (XMark.checked) {
            Game.userMark = 'X';
        } else if (OMark.checked) {
            Game.userMark = 'O';
        } else {
            formValidated = false;
        }
        let boardSize10 = document.getElementById('board-size-10');
        let boardSize15 = document.getElementById('board-size-15');
        if (boardSize10.checked) {
            Game.boardSize = 10;
        } else if (boardSize15.checked) {
            Game.boardSize = 15;
        } else {
            formValidated = false;
        }
        let easy = document.getElementById('easy');
        let medium = document.getElementById('medium');
        let hard = document.getElementById('hard');
        if (easy.checked) {
            Game.difficultyLevel = 'easy';
        } else if (medium.checked) {
            Game.difficultyLevel = 'medium';
        } else if (hard.checked) {
            Game.difficultyLevel = 'hard';
        } else {
            formValidated = false;
        }
        if (formValidated) {
            Game.userTurn = true;
            Game.playing = true;
            Game.fieldSize = (Game.canvasSize - Game.lineWidth * (Game.boardSize - 1)) / Game.boardSize;
            Game.board = [];
            for (let i = 0; i < Game.boardSize; ++i) {
                Game.board.push([]);
                for (let j = 0; j < Game.boardSize; ++j) {
                    Game.board[i].push(' ');
                }
            }
            Game.drawBoard();
        }
    },
    userMove: function (e) {
        if (Game.playing) {
            let x = Math.floor(e.offsetX / (Game.fieldSize + Game.lineWidth));
            let y = Math.floor(e.offsetY / (Game.fieldSize + Game.lineWidth));

            if (Game.board[x][y] === ' ') {
                if (Game.userTurn) {                    //only for both players in the browser
                    Game.board[x][y] = Game.userMark;   //
                    console.log('user move: ' + x + ' ' + y);
                } else {
                    if (Game.userMark === 'X') {      //
                        Game.board[x][y] = 'O';      //
                    } else {
                        Game.board[x][y] = 'X';
                    }
                    console.log('computer move: ' + x + ' ' + y);
                }                                     //
                Game.drawMark(x, y);
                console.log('ok');
                if (Game.userTurn) //only for both players in browser
                    if (Game.checkIfWin(x, y)) {
                        Game.playing = false;
                        console.log('User won!');
                        Game.drawWinningLine(x, y);
                    }
                Game.userTurn = !Game.userTurn; //this should only be uncommented when making both user's and computer's moves in the browser
                //Game.userTurn = false;
            } else {
                console.log('cannot make move');
            }
        }
    },
    computerMove: function (x, y, victory) { //this method is to be called when the computer's move is received from the server
        Game.drawMark(x, y);
        Game.userTurn = true;
        if (victory) {
            alert('Computer won!');
        }
    },
    drawMark: function (x, y) {
        if (this.userTurn) {
            this.ctx.strokeStyle = 'red';
        } else {
            this.ctx.strokeStyle = 'green';
        }
        if (this.userTurn && this.userMark === 'X' || !this.userTurn && this.userMark === 'O') {
            this.ctx.beginPath();
            this.ctx.moveTo(this.fieldPadding + x*(this.fieldSize + this.lineWidth), this.fieldPadding + y*(this.fieldSize + this.lineWidth));
            this.ctx.lineTo(x*(this.fieldSize + this.lineWidth) + this.fieldSize - this.fieldPadding, y*(this.fieldSize + this.lineWidth) + this.fieldSize - this.fieldPadding);
            this.ctx.stroke();
            this.ctx.beginPath();
            this.ctx.moveTo(x*(this.fieldSize + this.lineWidth) + this.fieldSize - this.fieldPadding, this.fieldPadding + y*(this.fieldSize + this.lineWidth));
            this.ctx.lineTo(this.fieldPadding + x*(this.fieldSize + this.lineWidth), y*(this.fieldSize + this.lineWidth) + this.fieldSize - this.fieldPadding);
            this.ctx.stroke();
        } else {
            this.ctx.beginPath();
            this.ctx.arc(
                x*(this.fieldSize + this.lineWidth) + this.fieldSize*0.5,
                y*(this.fieldSize + this.lineWidth) + this.fieldSize*0.5,
                this.fieldSize*0.5 - this.fieldPadding,
                0,
                2*Math.PI
            );
            this.ctx.stroke();
        }
    },
    checkIfWin: function (x, y) {
        //vertical line check
        let count = 1 + this.crawl(x, y, 0, 1) + this.crawl(x, y, 0, -1);
        console.log('vertical: ' + count);
        if (count >= this.marksToWin) {
            return true;
        }
        //horizontal
        count = 1 + this.crawl(x, y, 1, 0) + this.crawl(x, y, -1, 0);
        console.log('horizontal: ' + count);
        if (count >= this.marksToWin) {
            return true;
        }
        //diagonal top-down
        count = 1 + this.crawl(x, y, 1, 1) + this.crawl(x, y, -1, -1);
        console.log('diagonal t-d: ' + count);
        if (count >= this.marksToWin) {
            return true;
        }
        //diagonal down-top
        count = 1 + this.crawl(x, y, 1, -1) + this.crawl(x, y, -1, 1);
        console.log('diagonal d-t: ' + count);

        return count >= this.marksToWin;
    },
    crawl: function (x, y, directionX, directionY) {
        if (x + directionX >= 0 && y + directionY >= 0 &&
            x + directionX < this.boardSize && y + directionY < this.boardSize &&
            this.board[x + directionX][y + directionY] === this.userMark) {
            return 1 + this.crawl(x + directionX, y + directionY, directionX, directionY);
        } else {
            return 0;
        }
    },
    drawWinningLine: function () {
        return 0;
    }
};
Game.init();
