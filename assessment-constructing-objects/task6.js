class ListaDeCompras {
    constructor(){
        this.items = {};
    }

    agregarItem(item, cantidad = 1){
        this.items[item] = cantidad;
    }

    mostrarLista(){
        console.log("Tu lista de compras:");
        for (const item in this.items){
            console.log(`${this.items[item]} ${item}`);
        }
    }
}

function crearLista(){
    const prompt = require('prompt-sync')();
    const lista = new ListaDeCompras();

    let seguirAgregando = true;
    while (seguirAgregando){
        const item = prompt("Ingrese el nombre del articulo o 'salir' para terminar : ");
        if (item.toLowerCase()=== 'salir'){
            seguirAgregando = false;
        }else{
            const cantidad = parseInt(prompt("Ingrese la cantidad: "));
            lista.agregarItem(item, cantidad);
        }
    }
    return lista;
}

const miLista = crearLista();

miLista.mostrarLista();
