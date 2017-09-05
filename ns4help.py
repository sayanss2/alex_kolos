#fIO=fileIO, nNde=numNode, tPrl=transportProtocol, tRn=timeRun

def checksyn(*argv):
    if 'start' in argv and len(argv) == 2:
        return True

def gethelp(*argv, **kwargs):
    ptext = ''
    for i in argv:
        if len(argv) == 1:
            ptext = '\nNo such arguments!\nPlease help for list of files!'
            break
        if '-h' in i and len(argv) == 2:
            ptext = """
                COMMAND [opt]
                start      Start new model
                --files    Print list of files
                --node     Print num of node
                --proto    Print type of protocol"""
        elif '--files' in i:
            for i in kwargs.get('f_io'):
                ptext = ptext + '\n' + ('argv: {0}'.format(i))
        elif '--node' in i:
            ptext = ptext + '\n' + ('argv: {0}'.format(kwargs.get('n_nde')))
        elif '--proto' in i:
            ptext = ptext + '\n' + ('argv: {0}'.format(kwargs.get('t_prl')))
        else:
            if i != argv[0]:
                ptext = '\n Invalid arguments!'
                break
    print(ptext + '\n\n')
    
def errreport(*argv):
    print(argv[0])