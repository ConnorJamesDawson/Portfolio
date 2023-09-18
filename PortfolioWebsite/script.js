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

const navBtn = document.querySelectorAll(".navBtn");

let ripple;
navBtn.forEach(btn => {
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

const aboutMeText = document.querySelector(".aboutMeText");
const aboutMeTextContent = "Hello and welcome to my Porfolio website that I have made using HTML, CSS and Java. \nThis Website showcases my projects that I have done, Links to my GitHub profile and allows you to contact me.";

Array.from(aboutMeTextContent).forEach(char => 
    {
        const span = document.createElement('span');
        span.textContent = char;
        aboutMeText.appendChild(span);
    });

const container = document.querySelector('.container');
const projects = document.querySelectorAll(".project");
const projectHideBtn = document.querySelector(".projectHideBtn");

projects.forEach((project, i) =>{
    project.addEventListener('mouseenter', () =>
    {
        project.firstElementChild.style.top = `-${project.firstElementChild.offsetheight - project.offsetheight + 20}px`;
    });

    project.addEventListener('mouseleave', () =>
    {
        project.firstElementChild.style.top = "2rem";
    });

    project.addEventListener('click', () =>
    {
        const bigImgWrapper = document.createElement('div');
        bigImgWrapper.className = 'projectImgWrapper';
        container.appendChild(bigImgWrapper);

        const bigImg = document.createElement("img");
        bigImg.className = "projectImg";
        const imgPath = project.children[1].getAttribute("src"); //First child is title so need to select 2nd one
        bigImg.setAttribute("src", `${imgPath}`);
        bigImgWrapper.appendChild(bigImg);
        document.body.style.overflowY = "hidden";

        projectHideBtn.classList.add("change");

        projectHideBtn.onclick = () => {
            projectHideBtn.classList.remove("change");
            bigImgWrapper.remove();
            document.body.style.overflowY = "scroll";
        }
    });

    i >= 3 && (project.style.cssText = "display: none; opacity: 0");
    
});
const sectionThree = document.querySelector(".sectionThree");
const projectsBtn = document.querySelector(".projectsBtn");
const projectsBtnText = document.querySelector(".projectsBtn span");

let showHide = true;

const showProjects = (project, i) =>
{
    setTimeout(() => 
    {
        project.style.display = "flex";
        sectionThree.scrollIntoView({block: "end"})
    }, 600);

    setTimeout(() => {
        project.style.opacity = "1";
    }, i * 200);
};

const hideProjects = (project, i) =>
{
    setTimeout(() =>{
        project.style.display = "none";
        sectionThree.scrollIntoView({block: "end"})
    }, 1200);

    setTimeout(() => {
        project.style.opacity = "0";
    }, i * 100);
};

projectsBtn.addEventListener("click", (e) =>{
    e.preventDefault();

    projectsBtn.firstElementChild.nextElementSibling.classList.toggle("change");

    showHide ? (projectsBtnText.textContent = "Show Less") : (projectsBtnText.textContent = "Show More");

    projects.forEach((project, i) =>
    {
        i >= 3 && (showHide ? showProjects(project, i) : hideProjects(project, i));
    });

    showHide = !showHide;
});

document.querySelectorAll(".serviceBtn").forEach((service)=>{
    service.addEventListener('click', (e) => {
        e.preventDefault();

        const serviceText = service.nextElementSibling;
        serviceText.classList.toggle("change");

        const rightPosition = serviceText.classList.contains("change") ? `calc(100% - ${getComputedStyle(service.firstElementChild).width})` : 0;
        service.firstElementChild.style.right = rightPosition;
    });
});