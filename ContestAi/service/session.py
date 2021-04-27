def isAuthenticated(request):
    try:
        result = request.session['user']
        return True
    except:
        return False

registerStatus= {
    'Pending':'Pending',
    'Fail':'Fail',
    'Success': 'Success'
}