def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (sorted([yourLeft, yourRight]) == sorted([friendsLeft, friendsRight]))