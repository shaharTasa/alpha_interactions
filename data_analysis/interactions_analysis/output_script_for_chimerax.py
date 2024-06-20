
def generate_commands(tuples):
    commands = []
    for t in tuples:
        if t[0] == 'A':
            command1 = f"sel /A:{t[2]} ; color sel green ; label sel residues color black bgColor yellow text ""{0.name}{0.number}"" height 0.8 offset -2,1,0 "
            commands.append(command1)
        elif t[0] =='B':
            command1 = f"sel /B:{t[2]} ; color sel green ; label sel residues color black bgColor light grey text ""{0.name}{0.number}"" height 0.8 offset -2,1,0"
            commands.append(command1)
    return commands


def writing_commends_to_file_and_create_button(inter_chain_interactions):
    myfile = open('xyz.txt', 'w')
    commends=generate_commands(inter_chain_interactions)
    for commend in commends:
        myfile.write("%s\n" % commend)

    # commends=generate_commands(inter_chain_interactions)
    # for commend in commends:
    #     print(commend)
        
