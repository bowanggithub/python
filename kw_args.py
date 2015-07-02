def print_scores(**kw):
    print("         Name    Score")
    print("----------------------")
    for name,score in kw.items():
        print("%10s   %d" % (name,score))
    print()


print_scores(Adam=99,Lisa=88,Bart=77)

data={"Adam Lee": 99, "Lisa, S": 88, "F.Bart": 77}

print_scores(**data)



def print_info(name, *, gender, city="Beijing", age):
    print("personal info")
    print("---------------")
    print("   name: %s" % name)
    print("   gender: %s" % gender)
    print("   city: %s" % city)
    print("   age: %s" % age)
    print()

print_info("Bob", gender = "male", age=20)
print_info("Lisa", gender="female", city="Shanghai", age=18)
