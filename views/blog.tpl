% rebase('base.tpl')

%for idx, post in enumerate(posts):
  <div class="blog-post">
      <h2 class="blog-post-title">{{post['TITLE']}}</h2>
      <p class="blog-post-meta">{{post['POST_DATE']}} by <a href="#">{{post['AUTHOR']}}</a></p>
      <p>{{post['CONTENT']}}</p>
  </div>
%end

