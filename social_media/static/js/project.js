// /* Project specific Javascript goes here. */

// const blogDiv = document.querySelectorAll('.blog-post')

// blogDiv.forEach(function (div){
//     div.addEventListener('click',function(){
//         postId = div.id 
//         console.log(`Blog ${postId}`);
//         window.location.href= '/blog/blog_info/'+postId+'/'        

//     })
// })

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
