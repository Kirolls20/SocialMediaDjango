// read more
document.querySelectorAll('.read-more-link').forEach(function(link) {
    link.addEventListener('click', function(event) { 
      event.preventDefault();
      const truncatedText = this.parentElement;
      const fullText = truncatedText.nextElementSibling;
      
      truncatedText.style.display = 'none';
      fullText.style.display = 'block';
      // read less 
      const readLessLink = document.querySelectorAll('.read-less-link').forEach(link =>{
        link.style.display= 'block';
        link.addEventListener('click',function(event){
            event.preventDefault();
            fullText.style.display='none';
            truncatedText.style.display= 'block';
            link.style.display = 'none';
        })
      });
    });
  });
