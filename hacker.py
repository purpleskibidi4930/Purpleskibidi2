for x in range(1000):
    open("file%03d.txt" % x,"w").write("some text")
