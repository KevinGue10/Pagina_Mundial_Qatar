
//boton0
const myInput = document.getElementById("my-input");
function stepper(btn){
    let id = btn.getAttribute("id");
    let min = myInput.getAttribute("min");
    let max = myInput.getAttribute("max");
    let step = myInput.getAttribute("step");
    let val = myInput.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput.setAttribute("value", newValue);
    }
}

//boton1
const myInput1 = document.getElementById("my-input1");
function stepper1(btn){
    let id = btn.getAttribute("id");
    let min = myInput1.getAttribute("min");
    let max = myInput1.getAttribute("max");
    let step = myInput1.getAttribute("step");
    let val = myInput1.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput1.setAttribute("value", newValue);
        golV=newValue;
    }
}

//boton2
const myInput2 = document.getElementById("my-input2");
function stepper2(btn){
    let id = btn.getAttribute("id");
    let min = myInput2.getAttribute("min");
    let max = myInput2.getAttribute("max");
    let step = myInput2.getAttribute("step");
    let val = myInput2.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput2.setAttribute("value", newValue);
        remate=newValue;
    }
} 

//boton3
const myInput3 = document.getElementById("my-input3");
function stepper3(btn){
    let id = btn.getAttribute("id");
    let min = myInput3.getAttribute("min");
    let max = myInput3.getAttribute("max");
    let step = myInput3.getAttribute("step");
    let val = myInput3.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput3.setAttribute("value", newValue);
        remateV=newValue;
    }
} 

//boton4
const myInput4 = document.getElementById("my-input4");
function stepper4(btn){
    let id = btn.getAttribute("id");
    let min = myInput4.getAttribute("min");
    let max = myInput4.getAttribute("max");
    let step = myInput4.getAttribute("step");
    let val = myInput4.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput4.setAttribute("value", newValue);
        TaAm=newValue;
    }
} 

//boton5
const myInput5 = document.getElementById("my-input5");
function stepper5(btn){
    let id = btn.getAttribute("id");
    let min = myInput5.getAttribute("min");
    let max = myInput5.getAttribute("max");
    let step = myInput5.getAttribute("step");
    let val = myInput5.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput5.setAttribute("value", newValue);
        TaAmV=newValue;
    }
} 

//boton6
const myInput6 = document.getElementById("my-input6");
function stepper6(btn){
    let id = btn.getAttribute("id");
    let min = myInput6.getAttribute("min");
    let max = myInput6.getAttribute("max");
    let step = myInput6.getAttribute("step");
    let val = myInput6.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput6.setAttribute("value", newValue);
        TaRo=newValue;
    }
} 


//boton7
const myInput7 = document.getElementById("my-input7");
function stepper7(btn){
    let id = btn.getAttribute("id");
    let min = myInput7.getAttribute("min");
    let max = myInput7.getAttribute("max");
    let step = myInput7.getAttribute("step");
    let val = myInput7.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput7.setAttribute("value", newValue);
        TaRoV=newValue;
    }
} 

//boton8
const myInput8 = document.getElementById("my-input8");
function stepper8(btn){
    let id = btn.getAttribute("id");
    let min = myInput8.getAttribute("min");
    let max = myInput8.getAttribute("max");
    let step = myInput8.getAttribute("step");
    let val = myInput8.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput8.setAttribute("value", newValue);
        TidEs=newValue;
    }
} 

//boton9
const myInput9 = document.getElementById("my-input9");
function stepper9(btn){
    let id = btn.getAttribute("id");
    let min = myInput9.getAttribute("min");
    let max = myInput9.getAttribute("max");
    let step = myInput9.getAttribute("step");
    let val = myInput9.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <= max){
        myInput9.setAttribute("value", newValue);
        TidEsV=newValue;
    }
} 
