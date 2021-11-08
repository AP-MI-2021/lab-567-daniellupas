from Tests.testCRUD import testAdaugaCarte, testStergeCarte
from Tests.testDomain import testCarte
from Tests.testFunctions import testAplicaDiscount, testModificareGen, testPretMinimPeGen, testOrdonareDupaPret, \
    testDeterminareCartiCuTitluriDistincte


def runAllTests():

    testCarte()
    testAdaugaCarte()
    testStergeCarte()
    testAplicaDiscount()
    testModificareGen()
    testPretMinimPeGen()
    testOrdonareDupaPret()
    testDeterminareCartiCuTitluriDistincte()
