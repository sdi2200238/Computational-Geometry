def cross(o, a, b):
    """
    Υπολογισμός του διανυσματικού γινομένου των διανυσμάτων OA και OB.
    
    Είσοδος: Τρία σημεία o, a, b ως (x, y) συντεταγμένες.
    Έξοδος: Το διανυσματικό γινόμενο των διανυσμάτων OA και OB.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def distance_to_line(p1, p2, p):
    """
    Υπολογισμός της απόστασης ενός σημείου από μια ευθεία.
    
    Είσοδος: Τρία σημεία p1, p2, p ως (x, y) συντεταγμένες.
    Έξοδος: Η απόσταση του σημείου p από την ευθεία που ορίζεται από τα σημεία p1 και p2.
    """
    return abs(cross(p1, p2, p)) / ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
