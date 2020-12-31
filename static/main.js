const checkedBtn = document.getElementById("checked");
const todoItem = document.getElementById("todo")
checkedBtn.addEventListener("change",()=>{
    const checked = this.checked;
    if(checked){
        todoItem.classList.add("completed")

    }
    else if(!checked){
        todoItem.classList.remove("completed")

    }
   
})