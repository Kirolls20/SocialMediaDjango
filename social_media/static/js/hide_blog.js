function hideBlog(blogId){
    
    var blogId = document.getElementById('blog-' + blogId);
    var hiddenMessage = blogId.querySelector('.hidden-message')
    blogId.parentElement.parentElement.parentElement.style.animationPlayState = 'running';
    blogId.parentElement.parentElement.parentElement.addEventListener('animationend',function(){
      blogId.parentElement.parentElement.parentElement.remove()
    })
 }