var xBall = 200;
var yBall = 200;
var diameter = 25;

var xBallChange = 5;
var yBallChange = 1;

var xPaddleA = 20;
var yPaddleA = 200;

var xPaddleB = 780;
var yPaddleB = 200;

var paddleWidth = 10;
var paddleHeight = 75;

var paddleSpeed = 20;

//var started = false;

var scoreA = 0;
var scoreB = 0;

function setup() {
  createCanvas(800,400);
  rectMode(CENTER);
  noStroke(0);
}

function draw() {
  background(0);
  ballChange();
  wallCollision();
  paddleAHit();
  paddleBHit();
  //gameStart();
  paddleA();
  paddleB();
  scoreGame();
  ellipse(xBall,yBall,diameter);
}

// function gameStart(){
//     if (!started) {
//     xPaddleA = 25;
//     yPaddleA = height / 2;
//     xPaddleB = width - 25;
//     yPaddleB = height / 2;
//     started = true;
//   }
// }

function paddleA(){
  rect(xPaddleA,yPaddleA,paddleWidth,paddleHeight);
}

function paddleB(){
  rect(xPaddleB,yPaddleB,paddleWidth,paddleHeight);
}

function ballChange(){
  xBall += xBallChange;
  yBall += yBallChange;
}

function wallCollision(){
//if the x coordinate of the ball is less than the radius of the ball or greater than the width of the canvas width plus radius for a nicer bounce
 if (xBall < diameter/2 || xBall > 800 - 0.5*diameter) {
  xBallChange *= -1;
}
//else if the y coordinate of the ball is less than the radius or greater than the canvas height minus radius
if (yBall < diameter/2 || yBall > 400 - diameter/2) {
  yBallChange *= -1;
} 
}

function paddleAHit(){
   if ((yBall > yPaddleA ||
      yBall < yPaddleA + paddleHeight) &&
      (xBall - (diameter/2) <= xPaddleA + paddleWidth)) {
  xBallChange *= -1;
  yBallChange *= -1;
  scoreA++;
}
}

function paddleBHit(){
   if ((yBall > yPaddleB ||
      yBall < yPaddleB + paddleHeight) &&
      (xBall + (diameter/2) <= xPaddleB)) {
  xBallChange *= -1;
  yBallChange *= -1;
  scoreB++;
}
}

function scoreGame(){
  fill(255,255,255);
  textSize(72);
  text(scoreA, 200, 100);
  text(scoreB, 500, 100);
}

function keyPressed() {
  if (key == "a") {
    yPaddleA -= paddleSpeed;
  } else if (key == "z") {
    yPaddleA += paddleSpeed;
  }
  yPaddleA = constrain(yPaddleA,paddleHeight/2, height - paddleHeight/2);
  if (key == "l") {
    yPaddleB -= paddleSpeed;
  } else if (key == ",") {
    yPaddleB += paddleSpeed;
  }
  yPaddleB = constrain(yPaddleB,paddleHeight/2, height - paddleHeight/2);
}
