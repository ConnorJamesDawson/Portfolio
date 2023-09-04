const mouseCursor = document.querySelector(".mouseCircle");
const mouseCursorDot = document.querySelector(".mouseDot");

mouseCircleFn = (x, y)=>{

    mouseCursor.style.cssText = `top: ${y}px; left:${x}px; opacity: 1`;
    mouseCursorDot.style.cssText = `top:${y}px; left:${x}px; opacity: 1`;
};

document.body.addEventListener('mousemove', (e) => {
    let x = e.clientX;
    let y = e.clientY;

    mouseCircleFn(x, y);
});

document.body.addEventListener('mouseleave', () => {
    mouseCursor.style.opacity = '0';
    mouseCursorDot.style.opacity = '0';
})