import diagnost


def main():
    global d
    t = diagnost.Therapist()

    print("Welcome to the Therapist! \n")
    print("Please enter y(means yes) or n(means no) to questions provided")

    type_soma = input("is your disease somatically related?")
    if type_soma == "y":
        t.symptoms["type"] = "soma"
        headache = input("do you have a headache?")
        if headache == "y":
            t.symptoms["headache"] = True
            d = t.diagnose()
        elif headache == "n":
            t.symptoms["headache"] = False
            cough = input("do you cough?")
            if cough == "y":
                t.symptoms["cough"] = True
                ls = input("do you have a smell loose?")
                if ls == "y":
                    t.symptoms["loose_smell"] = True
                    d = t.diagnose()
                else:
                    t.symptoms["loose_smell"] = False
                    d = t.diagnose()
            else:
                t.symptoms["cough"] = False
                ls = input("do you have a smell")
                if ls == "y":
                    t.symptoms["loose_smell"] = True
                    d = t.diagnose()
                else:
                    t.symptoms["loose_smell"] = False
                    d = t.diagnose()
    elif type_soma == "n":
        type_psychology = input("is your disease psy related?")
        if type_psychology == "y":
            t.symptoms["type"] = "psycho"
            hal = input("do you have hallucinations?")
            if hal == "y":
                t.symptoms["hal"] = True
                d = t.diagnose()
            else:
                t.symptoms["hal"] = False
                dep = input("do you have bad mood?")
                if dep == "y":
                    t.symptoms["bad_mood"] = True
                    d = t.diagnose()
                else:
                    t.symptoms["bad_mood"] = False
                    d = t.diagnose()
        else:
            t.symptoms["type"] = None
            d = t.diagnose()

    print(d)


if __name__ == '__main__':
    main()
