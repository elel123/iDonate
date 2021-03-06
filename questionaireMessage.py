def questionareMessage():
    '''determines the messsage output based on their responses'''
    statementNotEligible = "Sorry, but you are not eligible to donate blood at this time. Please contact American Red Cross directly if you have further questions."
    statementEligible = "Congraulations! You are eligible to donate blood!"
    statementMaybeEligible = "You may still be able to donate. Please check the American Red Cross Website to see if your specific medication  is eligible."
    if "yes" in {q2, q3, q5, q7}:
        statement = statementNotEligible
        eligible = "no"
        return [statement, eligible]

    elif "no" in {q4, q6}:
        statement = statementNotEligible
        eligible = "no"
        return [statement, eligible]

    elif q8 == "yes":
        statement = statementMaybeEligible
        eligible = "yes"
        return [statement, eligible]
    
    else:
        statement = statementEligible
        eligible = "yes"
        return [statement, eligible]
