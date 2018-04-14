var Game = {
    userTurn: true,
    userMark: 'X',
    boardSize: 10,
    canvasSize: 500,
    lineWidth: 1,
    fieldPadding: 7,
    board: [],
    init: function () {
        console.log('initializing...');
        this.myCanvas = document.getElementById('my-canvas');
        this.myCanvas.width = this.canvasSize;
        this.myCanvas.height = this.canvasSize;
        this.ctx = this.myCanvas.getContext('2d');
        this.ctx.lineWidth = this.lineWidth;
        this.fieldSize = (this.canvasSize - this.lineWidth*(this.boardSize - 1))/this.boardSize;
        this.myCanvas.addEventListener('click', this.userMove, false);
        for (var i = 0; i < this.boardSize; ++i) {
            this.board.push([]);
            for (var j = 0; j < this.boardSize; ++j) {
                this.board[i].push(' ');
            }
        }
        //
        this.drawBoard();
    },
    drawBoard: function () {
        console.log('drawing board');
        for (var i = 0; i < 9; ++i) {
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
    userMove: function (e) {
        var x = Math.floor(e.offsetX/(Game.fieldSize + Game.lineWidth));
        var y = Math.floor(e.offsetY/(Game.fieldSize + Game.lineWidth));
        console.log('user move: ' + x + ' ' + y);
        if (Game.board[x][y] === ' ') {
            Game.board[x][y] = Game.userMark;
            Game.drawMark(x, y);
            Game.userTurn = !Game.userTurn; //this should only be uncommented when making both user's and computer's moves in the browser
            //Game.userTurn = false;
            console.log('ok');
            Game.checkIfWin(x, y);
        } else {
            console.log('cannot make move');
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
        var count = 0;

    }
}
Game.init();
