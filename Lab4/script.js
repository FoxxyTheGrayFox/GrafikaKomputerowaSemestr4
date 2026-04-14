const canvas = document.getElementById("canvas");
const gl = canvas.getContext("webgl2");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

gl.enable(gl.DEPTH_TEST);
gl.enable(gl.PROGRAM_POINT_SIZE);

// shader
const vs = `#version 300 es
layout(location=0) in vec3 aPos;
layout(location=1) in vec3 aCol;
layout(location=2) in float aSize;

uniform mat4 MVP;
out vec3 vCol;

void main(){
    gl_Position = MVP * vec4(aPos,1.0);
    gl_PointSize = aSize;
    vCol = aCol;
}`;

const fs = `#version 300 es
precision mediump float;
in vec3 vCol;
out vec4 fCol;

void main(){
    fCol = vec4(vCol,1.0);
}`;

function compile(type, src){
    const s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    return s;
}

const prog = gl.createProgram();
gl.attachShader(prog, compile(gl.VERTEX_SHADER, vs));
gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, fs));
gl.linkProgram(prog);
gl.useProgram(prog);

const uMVP = gl.getUniformLocation(prog, "MVP");


let objectNumber = 1;
let rotX = 0, rotY = 0;
let N = 3;

window.onkeydown = (e) => {
    if(e.key === "1") objectNumber = 1;
    if(e.key === "2") objectNumber = 2;

    if(e.key === "ArrowUp") rotX += 0.1;
    if(e.key === "ArrowDown") rotX -= 0.1;
    if(e.key === "ArrowLeft") rotY += 0.1;
    if(e.key === "ArrowRight") rotY -= 0.1;
};

// kamera
function perspective(fovy, aspect, near, far){
    const f = 1 / Math.tan(fovy / 2);
    return new Float32Array([
        f/aspect,0,0,0,
        0,f,0,0,
        0,0,(far+near)/(near-far),-1,
        0,0,(2*far*near)/(near-far),0
    ]);
}

function translate(z){
    return new Float32Array([
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        0,0,z,1
    ]);
}

function rotXf(a){
    const c=Math.cos(a), s=Math.sin(a);
    return new Float32Array([
        1,0,0,0,
        0,c,s,0,
        0,-s,c,0,
        0,0,0,1
    ]);
}

function rotYf(a){
    const c=Math.cos(a), s=Math.sin(a);
    return new Float32Array([
        c,0,-s,0,
        0,1,0,0,
        s,0,c,0,
        0,0,0,1
    ]);
}

function multiply(a,b){
    const r = new Float32Array(16);
    for(let i=0;i<4;i++){
        for(let j=0;j<4;j++){
            r[j*4+i] =
                a[i] * b[j*4] +
                a[i+4] * b[j*4+1] +
                a[i+8] * b[j*4+2] +
                a[i+12] * b[j*4+3];
        }
    }
    return r;
}

// VAO
function createVAO(data){
    const vao = gl.createVertexArray();
    const vbo = gl.createBuffer();

    gl.bindVertexArray(vao);
    gl.bindBuffer(gl.ARRAY_BUFFER, vbo);
    gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);

    const stride = 7 * 4;

    gl.vertexAttribPointer(0,3,gl.FLOAT,false,stride,0);
    gl.enableVertexAttribArray(0);

    gl.vertexAttribPointer(1,3,gl.FLOAT,false,stride,12);
    gl.enableVertexAttribArray(1);

    gl.vertexAttribPointer(2,1,gl.FLOAT,false,stride,24);
    gl.enableVertexAttribArray(2);

    return { vao, count: data.length / 7 };
}

// korkociąg
function createCorkscrew(){
    const data = [];
    const points = 200;
    const radius = 0.5;

    for(let i=0;i<points;i++){
        const t = i / points * N * Math.PI * 2;

        const x = radius * Math.cos(t);
        const y = i * 0.01;
        const z = radius * Math.sin(t);

        const col = [0.2, 0.5 + 0.5*Math.sin(t), 1.0];
        const size = 3;

        data.push(x,y,z, ...col, size);
    }

    return new Float32Array(data);
}

// piramida
function tri(out, a,b,c, col){
    out.push(...a, ...col, 1);
    out.push(...b, ...col, 1);
    out.push(...c, ...col, 1);
}

function pyramidBase(){
    const out = [];

    const center = [0,0,0];
    const col = [0.4,0.4,0.0];

    // środek
    const base = [];

    for(let i=0;i<N;i++){
        const a = i / N * Math.PI * 2;
        base.push([
            Math.cos(a),
            0,
            Math.sin(a)
        ]);
    }

    for(let i=0;i<N;i++){
        const a = base[i];
        const b = base[(i+1)%N];

        tri(out, center, a, b, col);
    }

    return out;
}

function pyramidSides(){
    const out = [];

    const top = [0, 1.5, 0];

    const base = [];

    for(let i=0;i<N;i++){
        const a = i / N * Math.PI * 2;
        base.push([
            Math.cos(a),
            0,
            Math.sin(a)
        ]);
    }

    for(let i=0;i<N;i++){
        const col = [
            1 - i/N,
            1 - i/N,
            0
        ];

        tri(out, base[i], base[(i+1)%N], top, col);
    }

    return out;
}

function createPyramid(){
    return new Float32Array([
        ...pyramidBase(),
        ...pyramidSides()
    ]);
}


const corkscrew = createVAO(createCorkscrew());
const pyramid = createVAO(createPyramid());

// render
function display(){
    gl.viewport(0,0,canvas.width,canvas.height);
    gl.clearColor(0,0,0,1);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    const proj = perspective(1.0, canvas.width/canvas.height, 0.1, 100);
    const view = translate(-6);

    const model = multiply(rotXf(rotX), rotYf(rotY));
    const mvp = multiply(proj, multiply(view, model));

    gl.uniformMatrix4fv(uMVP,false,mvp);

    const obj = objectNumber === 1 ? corkscrew : pyramid;

    gl.bindVertexArray(obj.vao);
    gl.drawArrays(
        objectNumber === 1 ? gl.POINTS : gl.TRIANGLES,
        0,
        obj.count
    );

    requestAnimationFrame(display);
}

display();