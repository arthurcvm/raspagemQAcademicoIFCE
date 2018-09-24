function Exibir_Aguarde() {
    return;
    layer_aguardar.style.pixelLeft = document.body.scrollLeft +
          ((document.body.clientWidth - layer_aguardar.clientWidth) / 2);
    layer_aguardar.style.pixelTop = document.body.scrollTop +
          ((document.body.clientHeight - layer_aguardar.clientHeight) / 2);
    layer_aguardar.style.visibility = 'visible'
}

function Disparar_Before_Unload_Customizado() {
    if (window.Before_Unload_Customizado) {
        return window.Before_Unload_Customizado();
    }
}

function KeyPressAscCode(e) {
    var key;
    var naoDeixaDigitar;

    key = e.which || e.keyCode;

    if (parseInt(key) === 0) {
        key = e.charCode;
    }

    naoDeixaDigitar = (isNaN(String.fromCharCode(key))) && !(parseInt(key) > 47 && parseInt(key) < 58)
                        && !(parseInt(key) === 44);

    if (naoDeixaDigitar) {
        return false;
    }

    return true;
}