const PromptSync = require("prompt-sync");

class FriendsList{
    constructor(){
        this.friends =[];
    }
    addFriend(name){
        this.friends.push(name);
    }
    printFriends(){
        console.log(this.friends);
    }
}
 
const prompt = require('Prompt-Sync')();
const numberOfFriends = parseInt(prompt("cantidad de amigos"))

const myFriends = new FriendsList();

for (let i = 0; i < numberOfFriends; i++){
    const friendName = prompt(`Nombre del amigo ${i + 1}: `);
    myFriends.addFriend(friendName);
}

myFriends.printFriends();