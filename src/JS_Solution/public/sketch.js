let engine = Matter.Engine.create();

let render = Matter.Render.create({
    element: document.body,
    engine: engine,
    options: {
        width: window.innerWidth,
        height: window.innerHeight,
        wideframes: false,
        showcollisions: true
    }
});

// engine.world.gravity.y = 0;

const windowWIDTH = render.bounds.max.x;
const windowHEIGHT = render.bounds.max.y;
const wallThickness = 300;

function getRect(x, y, width, height, isStatic=false) {
    this.x = x + width/2;
    this.y = y + height/2;
    this.width = width;
    this.height = height;
    if (isStatic) {
        return Matter.Bodies.rectangle(this.x, this.y, this.width, this.height, {isStatic: true});
    }
    options = {
        friction: 1,
        restitution: 1
    }
    return Matter.Bodies.rectangle(this.x, this.y, this.width, this.height);

}

let movable = getRect(windowWIDTH/2, windowHEIGHT/2, 60, 60);
// console.log(movable);

function updatePOS(res) {
    movable.position.x =  windowWIDTH - (res.x * windowWIDTH);
    movable.position.y = res.y * windowHEIGHT;
}

let ground_BOTTOM = getRect(0, windowHEIGHT, windowWIDTH, wallThickness, isStatic=true);
let ground_TOP = getRect(0, 0, windowWIDTH, -1*wallThickness, isStatic=true);
let ground_RIGHT = getRect(windowWIDTH, 0, wallThickness, windowHEIGHT, isStatic=true);
let ground_LEFT = getRect(0, 0, -1 * wallThickness, windowHEIGHT, isStatic=true);

let BoxA = Matter.Bodies.rectangle(400, 200, 80, 80);
let BoxB = Matter.Bodies.rectangle(450, 20, 80, 80);

// posX, posY, colsNum, rowsNum, gap b/w cols, gap b/w rows, call back func to create obj
let numRows = 5;
let numCols = 5;
let stack = Matter.Composites.stack(200, 200, numRows, numCols, 0, 0, (x, y) => {
    return Matter.Bodies.rectangle(x, y, 80, 80);
    // let sides = Math.round(Matter.Common.random(2, 8));
    // return Matter.Bodies.polygon(x, y, sides, Matter.Common.random(50, 60));
})

let mouse = Matter.Mouse.create(render.canvas);
let mouseConstraint = Matter.MouseConstraint.create(engine, {
    mouse: mouse,
    constraint: {
        render: {visible: false}
    }
});
render.mouse = mouse;


Matter.World.add(engine.world, [BoxA, BoxB, mouseConstraint, stack, ground_BOTTOM, ground_TOP, ground_LEFT, ground_RIGHT, movable]);
Matter.Engine.run(engine);
Matter.Render.run(render);