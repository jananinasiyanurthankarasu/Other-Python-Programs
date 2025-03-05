#String slicing in python to chck if a string can become empty by recursive deletion

main_string = "GeGeekseks"
sub_string = "Geeks"
while sub_string in main_string:
    main_string = main_string.replace(sub_string,"")

if len(main_string) == 0:
    print("True")
else:
    print("False")
