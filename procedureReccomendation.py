def recommendation():
    procedure1 = ""
    procedure2 = ""
    procedure3 = ""
    procedure4 = ""
    if q1 == "yes" and q10 in {'O-','O+','A-', 'B-'}:
        procedure1 = "(Recommended)"
        procedure2 = "(Highly Recommended if Height & Weight Met)"
        return [procedure1, procedure2, procedure3, procedure4]
        
    elif q11 == "no":
        procedure1 = "(Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
    
    elif q10 in {'O-','O+','A-', 'B-'}:
        procedure1 = "(Recommended)"
        procedure2 = "(Highly Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
    
    elif q10 in {'A+', 'B+'}:
        procedure1 = "(Recommended)"
        procedure3 = "(Highly Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
    
    elif q10 in {'AB+','AB-'}:
        procedure1 = "(Recommended)"
        procedure3 = "(Highly Recommended)"
        procedure4 = "(Highly Recommended)"
        return [procedure1, procedure2, procedure3, procedure4]
