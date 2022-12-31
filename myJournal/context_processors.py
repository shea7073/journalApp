from post.models import Post

def latest_date(request):
    context = {}
    if request.user.is_authenticated:
        try:
            obj = Post.objects.filter(owner=request.user).latest('post_date')
            field_object = Post._meta.get_field('post_date')
            field_value = field_object.value_from_object(obj)
            year = field_value.year
            day = field_value.day
            month = field_value.month
            context = {'post_day': day, 'month':month, 'year':year}
            return context
        except:
            context = {'post_day': 0, 'month': 0, 'year': 0}
            return context
    else:
        return context