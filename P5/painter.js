let circleX = 0;
let n = 1
let lineY = 0

function setup() {
  createCanvas(400, 400);
  background(0);
}

function draw() {
  fill(180,n,n);
  noStroke();
  circle(circleX, lineY,n-25);
  n = n + 0.01
  lineY = lineY + 0.1
  
  if (circleX <= 400) {
    circleX = circleX + n;
} else {
  circleX = circleX - 400;
}
}

function mousePressed(){
  circleX = 0
}