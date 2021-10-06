let bug = [];
let numberOfBugs = 1000;

function setup() {
  createCanvas(400, 400);
  for(let i = 0; let < numberOfBugs; i ++){
    bug.push(new Jitter());
  //bug.changeColor();
}

function draw() {
  background(150,150,200);
  for(let i = 0; let < numberOfBugs; i ++){
    bug.display();
    bug.move();
  }
  

class Jitter {
  constructor() {
    this.x = random(width);
    this.y = random(height);
    this.diameter = 50;
    this.speed = 2;
  }

  move(){
    this.x += random(-this.speed, this.speed);
    this.y += random(-this.speed, this.speed);
  }

  display(){
    ellipse(this.x ,this.y, this.diameter, this.diameter);
  }

  changeColor(){
    fill(random(255),random(255),random(255))
  }
}
