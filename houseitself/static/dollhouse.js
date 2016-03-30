function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    ev.target.parentNode.appendChild(ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    //numb = ev.target.childNodes[0].style.color; 
    //alert(numb);
    ev.target.appendChild(document.getElementById(data)); 
    document.getElementById(data).style="border-color: " + ev.target.childNodes[0].style.color + "; border-width: 5px; border-style: solid;"
    if (ev.target.childNodes.length > 1) {
    	ev.target.removeChild(ev.target.childNodes[0]);
    }
}


//reparenting
//draggable element
//JQuery ON

//mouseMovement events (if not using custom drag/drop stuff)


