from Tests.testCRUD import testAdaugaCarte, testStergeCarte
from Tests.testDomain import testCarte
from Tests.testFunctions import testAplicaDiscount, testModificareGen, testPretMinimPeGen, testOrdonareDupaPret, \
    testDeterminareCartiCuTitluriDistincte, test_undo_si_redo


def runAllTests():

    testCarte()
    testAdaugaCarte()
    testStergeCarte()
    testAplicaDiscount()
    testModificareGen()
    testPretMinimPeGen()
    testOrdonareDupaPret()
    testDeterminareCartiCuTitluriDistincte()
    test_undo_si_redo()

