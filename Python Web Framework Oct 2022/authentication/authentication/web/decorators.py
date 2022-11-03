from django.http import HttpResponse


def allow_groups(groups=None):
    if groups is None:
        groups = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponse('Not authenticated!')

            if request.user.is_superuser or not groups:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.filter(name__in=groups)

            # Never write raw SQL like this, risk of SQL Injection,
            # it should be like the above row with filter
            # User.objects.raw("SELECT * FROM ....")

            if not user_groups:
                return HttpResponse('Not in any of the allowed groups')

            return view_func(request, *args, **kwargs)

        return wrapper

    print(groups)
    if callable(groups):
        func = groups
        groups = []
        return decorator(func)

    return decorator


# To be able to use the below decorator in both ways,
# we need to construct it as above

# @allow_groups
# @allow_groups(groups=['Users'])
def index():
    pass
