print("BB-8 and R2D2")

print("R2D2 is a ____ and ______ _________ droid. R2 units were built to _____ humans and can ____________ and")
print("        (blank 1) ; (blank 2) ; (blank 3) ;                     ;(blank 4)              ;(blank 5)")
print("                                                                                                       ")
print("even ___________. R2D2 first served Queen _______ and went on to _____ Jedi ______ Luke ___ walker.")
print("      (blank 6)                          (blank 7)             (blank 8)   (blank 9)  (blank 10)")
print("                                                                                                       ")
print("BB-8 is BB series astromech _____ with a ____-shaped head like R2D2 and a body shaped like a _________.")
print("                         (blank 11)   (blank 12)                                             (blank 13)")
print("                                                                                                       ")
print("BB-8 is a _____ droid to Commander ___ Dameron. BB-8 and R2D2 _________ together to help __________")
print("        (blank 14)              (blank 15)                    (blank 16)                 (blank 17)")
print("                                                                                                       ")
print("the First Order")
print("                                                                                                       ")

key_1 = input("(blank 1),Enter a adjective; color :")
key_2 = input("(blank 2),Enter a adjective; color :")
key_3 = input("(blank 3),Enter a adjective :")
key_4 = input("(blank 4),Enter a verb :")
key_5 = input("(blank 5),Enter a verb :")
blank_6 = input("(blank 6),Enter a verb :")
blank_7 = input("(blank 7),Enter a noun; proper name :")
blank_8 = input("(blank 8),Enter a verb :")
blank_9 = input("(blank 9),Enter a noun :")
blank_10 = input("(blank 10),Enter a noun; place :")
blank_11 = input("(blank 11),Enter a noun :")
blank_12 = input("(blank 12),Enter a noun :")
blank_13 = input("(blank 13),Enter a noun :")
blank_14 = input("Enter a adjective :")
blank_15 = input("Enter a noun; first name :")
blank_16 = input("Enter a verb-ed :")
blank_17 = input("Enter a verb :")
print("                                                                                                       ")

answer_1 = "blue"
answer_2 = "white"
answer_3 = "astromech"
answer_4 = "serve"
answer_5 = "communicate"

if (key_1 == answer_1) and (key_2 == answer_2) and (key_3 == answer_3) and (key_4 == answer_4) and (key_5 == answer_5):
    print(f"R2D2 is a {key_1} and {key_2} {key_3} droid. R2 units were built to {key_4} humans and can {key_5}")
elif(key_1 != answer_1) and (key_2 == answer_2) and (key_3 == answer_3) and (key_4 == answer_4) and (key_5 == answer_5):
    print(f"R2D2 is a ____ and {key_2} {key_3} droid. R2 units were built to {key_4} humans and can {key_5}")
elif(key_1 == answer_1) and (key_2 != answer_2) and (key_3 == answer_3) and (key_4 == answer_4) and (key_5 == answer_5):
    print(f"R2D2 is a {key_1} and _____ {key_3} droid. R2 units were built to {key_4} humans and can {key_5}")
elif(key_1 == answer_1) and (key_2 == answer_2) and (key_3 != answer_3) and (key_4 == answer_4) and (key_5 == answer_5):
    print(f"R2D2 is a {key_1} and {key_2} _________ droid. R2 units were built to {key_4} humans and can {key_5}")
elif(key_1 == answer_1) and (key_2 == answer_2) and (key_3 == answer_3) and (key_4 != answer_4) and (key_5 == answer_5):
    print(f"R2D2 is a {key_1} and {key_2} {key_3} droid. R2 units were built to ___________ humans and can {key_5}")
else:
    print("R2D2 is a ____ and ______ _________ droid. R2 units were built to _____ humans and can ____________ ")
print(f"and even {blank_6}. R2D2 first served Queen {blank_7} and went on to {blank_8} Jedi {blank_9} Luke ")
print(f"{blank_10}walker. BB-8 is a BB series astromech {blank_11} with a {blank_12}-shaped head like R2D2 and a ")
print(f"body shaped like a {blank_13}. BB-8 is a {blank_14} droid to Commander {blank_15} Dameron. BB-8 and R2D2")
print(f"{blank_16} together to help {blank_17} the First Order.")
