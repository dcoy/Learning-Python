tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

no_color = "\x1b[0m"
green_bg = "\x1b[6;30;42m"

fat_cat = """
I'll do a list:
\t* {0}Cat food{1}
\t* Fishies
\t* Catnip\n\t* Grass
""".format(green_bg, no_color)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
