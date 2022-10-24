import pytest
from tests.fixtures.fixtures import fixture_tm


class TestVisualize:

    @pytest.mark.usefixtures('tm')
    def test_dummy(self):
        assert True

    @pytest.mark.usefixtures('tm')
    def test_visualize(self, tm):
        # Given il sistema è in idle e aspetta un comando utente
        # When l'utente vuole visualizzare tutti i task
        expected_output = '[ Task t1' \
                                 '\nTags [\'Android\', \'Java\']' \
                                 '\nProject App Android' \
                                 '\nDeadline 25/12/2020' \
                                 '\nStatus TODO ]'
        # Then i task vengono stampati a schermo
        assert tm.visualize() == expected_output
