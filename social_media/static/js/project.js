/* Project specific Javascript goes here. */

const blogDiv = document.querySelectorAll('.blog-post')

blogDiv.forEach(function (div){
    div.addEventListener('click',function(){
        postId = div.id 
        console.log(`Blog ${postId}`);
        window.location.href= '/blog/blog_info/'+postId+'/'        

    })
})