def isAuthenticated(request):
    try:
        result = request.session['user']
        return True
    except:
        return False