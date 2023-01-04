from django.contrib.auth.models import User
from .models import Blogs

def userExists(id):
    try:
        user = User.objects.get(id=id)
        return True
    except:
        return False
        
def blogExists(id):        
    try:
        blog = Blogs.objects.get(id=id)
        return True
    except:
        return False

def validateBlogCreation(postdata):
    bool = False
    if "title" and "content" and "author_id" in postdata:
        if userExists(postdata['author_id']):
            bool = True
            message = "Successful"
        else:
            message = "Author not found"
    else:
        message = "Send all required details"
    return {"bool":bool,"message":message}

def serializeBlogs(queryset):
    data = []
    for blog in queryset:
        temp = {}
        temp['title'] = blog.title
        temp['author'] = blog.author.username
        temp['content'] = blog.content
        temp['is_published'] = blog.is_published
        temp['published_at'] = blog.published_at
        temp['created_at'] = blog.created_at
        temp['updated_at'] = blog.updated_at
        data.append(temp)
    
    return data