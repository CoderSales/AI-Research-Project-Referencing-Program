def spacesList():
    import firstname # has allnames
    allnames=firstname.allnames()
    
    import firstname2 # has spacesInAuthorString
    spacesList=firstname2.spacesInAuthorString(allnames)
    
    return spacesList

# print(spacesList())
