
const deleteBtn = document.querySelectorAll('#delete');
const cancelBtns = document.querySelectorAll('#cancel');

deleteBtn.forEach(function(btn,index){
    btn.addEventListener('click',function(){
        const deleteContainer = document.querySelectorAll('.delete-container')[index];
        deleteContainer.style.display = 'block';
    })
    
});
cancelBtns.forEach(function (cancelBtn) {
    cancelBtn.addEventListener('click', function () {
        const parentDeleteContainer = cancelBtn.parentElement.parentElement;
        parentDeleteContainer.style.display = 'none';
    });
});


// Profile Page 
document.querySelector('#setting-btn').addEventListener('click',function(){
    document.querySelector('.setting-menu').style.display = 'block';
});

