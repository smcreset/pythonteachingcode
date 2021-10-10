code_tip = "code a conditional decision like you would say it"
print ("code_tip:" , code_tip)
i_index = code_tip.find("i")

while i_index != -1:
    print(code_tip.find("i", i_index))
    i_index = code_tip.find("i", i_index + 1)


