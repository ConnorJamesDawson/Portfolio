const mouseCursor = document.querySelector(".mouseCircle");
const mouseCursorDot = document.querySelector(".mouseDot");

mouseCircleFn = (x, y)=>{

    mouseCursor.style.cssText = `top: ${y}px; left:${x}px; opacity: 1`;
    mouseCursorDot.style.cssText = `top:${y}px; left:${x}px; opacity: 1`;
};

const circles = document.querySelectorAll(".circle");
const mainImg = document.querySelector(".mainCircle img");

let mX = 0;
let mY = 0;
const circleMovementpx = 50;

const animateCircles = (e, x, y) => {
    if(x < mX)
    {
        circles.forEach(circle =>
            {
                circle.style.left = `${circleMovementpx}px`;
            })
            mainImg.style.left = `${circleMovementpx}px`;
    }
    else if(x > mX)
    {
        circles.forEach(circle =>
            {
                circle.style.left = `-${circleMovementpx}px`;
            })
            mainImg.style.left = `-${circleMovementpx}px`;
    }
    if(y < mY)
    {
        circles.forEach(circle =>
            {
                circle.style.top = `${circleMovementpx}px`;
            })
            mainImg.style.top = `${circleMovementpx}px`;
    }
    else if(y > mY)
    {
        circles.forEach(circle =>
            {
                circle.style.top = `-${circleMovementpx}px`;
            })
            mainImg.style.top = `-${circleMovementpx}px`;
    }
    mX = e.clientX;
    mY = e.clientY;
}

document.body.addEventListener('mousemove', (e) => {
    let x = e.clientX;
    let y = e.clientY;

    mouseCircleFn(x, y);
    animateCircles(e, x, y);
});

document.body.addEventListener('mouseleave', () => {
    mouseCursor.style.opacity = '0';
    mouseCursorDot.style.opacity = '0';
})

const projectBtn = document.querySelectorAll(".projectBtn");

let ripple;
projectBtn.forEach(btn => {
    btn.addEventListener("mouseenter", (e) =>{
        const left = e.clientX - e.target.getBoundingClientRect().left;
        
        const top = e.clientY - e.target.getBoundingClientRect().top;
            
        ripple = document.createElement('div');
        ripple.classList.add("ripple");
        ripple.style.left = `${left}px`;
        ripple.style.top = `${top}px`;
        btn.prepend(ripple);
        });
        
        btn.addEventListener('mouseleave', () => {
            btn.removeChild(ripple);
        });
});

