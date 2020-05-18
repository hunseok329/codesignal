def variableName(name):
    try:
        int(name[0])
        return False
    except:
        if any(sym in name for sym in '!@#$%^&*()-+?><[]{}/.,;=\ '):
            return False
    return True
