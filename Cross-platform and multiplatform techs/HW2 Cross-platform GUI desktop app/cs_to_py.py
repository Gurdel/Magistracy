with open('Solver.cs') as sr, open('solver.py', 'w') as sw:
    code = sr.read()
    code = code.replace('{', '').replace('}', '').replace(';', '') \
                .replace('int', '').replace('double', '')
    sw.writelines(code)