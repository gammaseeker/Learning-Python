def getResponse(phrase):
    if(phrase[len(phrase) - 1] == "?" and len(phrase) % 2 == 0):
        return "Yes"
    else:
        if(phrase[len(phrase) - 1] == "?" and len(phrase) % 2 == 1):
            return "No"
        else:
            if(phrase[len(phrase) - 1] == "!"):
                return "Wow"
            else:
                return "You always say"

print(getResponse("Is it raining?"))