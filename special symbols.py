def function(normal, *argssimona, **kwargs):
    print (normal)
    for item in argssimona:
      print (item)

    print ("\nNow let us see what are Simona's fav Singers:")
    for key, value in kwargs.items():
        print (f"{key} is {value}")
name= ["Simona", "Likes", "To", "Sing"]
normal= "Let us know what Simona likes:"
kw= {"First":"Selena", "Second":"Doja", "Third":"Zayn"}
function(normal, *name, **kw)
