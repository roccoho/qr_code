const img_form = document.getElementById("img_form");
const qr_file = document.getElementById("qr_file");   


window.addEventListener('paste', e => {
    if (document.activeElement.id != "qr_img_url"){ 
        qr_blob = e.clipboardData.files; 
        if(typeof qr_blob !== "undefined"){  
            qr_file.files = qr_blob;  
            img_form.submit(); 
        } 
    }  
});  

document.getElementById("qr_file").onchange = function() {  
    img_form.submit(); 
};


function dropHandler(ev) {  
    ev.preventDefault(); 
    ev.stopPropagation();
    document.getElementById("drop_zone").style.backgroundColor = "";  
    qr_file.files = ev.dataTransfer.files; 
    img_form.submit();   
}

function dragOverHandler(ev) { 
    ev.preventDefault();
    ev.stopPropagation();
    document.getElementById("drop_zone").style.backgroundColor = "rgb(122, 136, 148)"; 
}

function dragLeaveHandler(ev){
    ev.preventDefault();
    ev.stopPropagation();
    document.getElementById("drop_zone").style.backgroundColor = "";
}

function dragEnterHandler(ev) { 
    ev.preventDefault();
    ev.stopPropagation();
    document.getElementById("drop_zone").style.backgroundColor = "rgb(122, 136, 148)"; 
}

function clickHandler(ev) {
    document.getElementById("qr_file").click();
}
