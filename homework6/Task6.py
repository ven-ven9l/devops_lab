import os
import json
import yaml
import unittest


class TestPyenv(unittest.TestCase):
    def test_pyenv(self, val):
        self.assertTrue('pyenv' in val)

    def testFalse(self, val1, val2):
        self.assertFalse(val1 == val2)


check = TestPyenv()
pyenv = os.popen('source $HOME/.bash_profile;which pyenv').readline()[:-1]
check.test_pyenv(pyenv)
p = os.popen(pyenv + ' versions', "r")
vers = []
res = {}
while 1:
    line = p.readline()
    if not line:
        break
    else:
        if line.split()[0] != '*':
            vers.append(line.split()[0])
        else:
            vers.append(line.split()[1])
check.testFalse(vers[0], vers[1])
for i in vers:
    path = os.popen(pyenv + ' local ' + i + ';' + pyenv + ' which python', "r")
    path = path.readline()[:-1]
    pip = os.popen(pyenv + ' which pip', "r")
    pip = pip.read()[:-1]
    pip_list = os.popen(pip + ' list --format=columns', "r")
    packs = {}
    locs = []
    it = 0
    while True:
        line = pip_list.readline()
        if not line:
            break
        else:
            if it > 1:
                packs[line.split()[0]] = line.split()[1]
        it += 1
    sp = os.popen(path + ' -m site', "r")
    v = os.popen(path + ' -c \'import sys; print(sys.version)\'', "r")
    v = v.readline()[:-1]
    it = 0
    while True:
        line = sp.readline()
        if (not line) | (']' in line):
            break
        else:
            if it > 1:
                locs.append(line.split('\'')[1])
        it += 1
    data = {
        'version': v,
        'path': path,
        'pip_path': pip,
        'modules': packs,
        'package_locations': locs
    }
    res[i] = data
    print("\nInfo about: ", i)
    print("-------------------------------------------")
    print("Version is        : ", v)
    print("Path is           : ", path)
    print("Pip path is       : ", pip)
    print("---------")
    print("Modules :")
    print("---------")
    print("{" + "\n".join("{}: {}".format(k, v) for k, v in packs.items()) + "}")
    print("---------")
    print("Package locations :")
    print("---------")
    for st in locs:
        print(st)
print("\nResult JSON :")
print(json.dumps(res, sort_keys=False, separators=(', ', ': ')) + "\n")
print("Result YAML :")
print(yaml.dump(res, default_flow_style=False, allow_unicode=True))
