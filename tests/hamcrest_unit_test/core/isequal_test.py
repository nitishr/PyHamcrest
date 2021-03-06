if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.core.core.isequal import *

from hamcrest_unit_test.matcher_test import MatcherTest
import unittest
import pytest
import six

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsEqualTest(MatcherTest):

    def testComparesObjectsUsingEquality(self):
        self.assert_matches('equal numbers', equal_to(1), 1)
        self.assert_does_not_match('unequal numbers', equal_to(1), 2)

    def testCanCompareNoneValues(self):
        self.assert_matches('None equals None', equal_to(None), None)

        self.assert_does_not_match('None as argument', equal_to('hi'), None)
        self.assert_does_not_match('None in equal_to', equal_to(None), 'hi')

    def testHonorsArgumentEqImplementationEvenWithNone(self):
        class AlwaysEqual:
            def __eq__(self, obj): return True
        class NeverEqual:
            def __eq__(self, obj): return False
        self.assert_matches("always equal", equal_to(None), AlwaysEqual())
        self.assert_does_not_match("never equal", equal_to(None), NeverEqual())

    def testIncludesTheResultOfCallingToStringOnItsArgumentInTheDescription(self):
        argument_description = 'ARGUMENT DESCRIPTION'
        class Argument:
            def __str__(self): return argument_description
        self.assert_description('<ARGUMENT DESCRIPTION>', equal_to(Argument()))

    def testReturnsAnObviousDescriptionIfCreatedWithANestedMatcherByMistake(self):
        inner_matcher = equal_to('NestedMatcher')
        self.assert_description("<'NestedMatcher'>", equal_to(inner_matcher))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(equal_to('hi'), 'hi')

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", equal_to('good'), 'bad')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", equal_to('good'), 'bad')

    def testEqualToWithEqualBytes(self):
        self.assert_matches("equal for b", equal_to(six.b('a')), six.b('a'))

    def testNotEqualToWithEqualBytes(self):
        self.assert_does_not_match("equal for b", equal_to(six.b('a')), six.b('b'))

    @pytest.mark.skipif(six.PY2, reason="Py3 formatting")
    def testByteInequalityDescriptionPy3(self):
        self.assert_mismatch_description("was <{0!r}>".format(six.b('b')), equal_to(six.b('a')), six.b('b'))

    @pytest.mark.skipif(six.PY3, reason="Py2 formatting")
    def testByteInequalityDescriptionPy2(self):
        self.assert_mismatch_description("was {0!r}".format(six.b('b')), equal_to(six.b('a')), six.b('b'))


if __name__ == '__main__':
    unittest.main()
