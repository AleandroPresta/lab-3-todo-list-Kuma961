import pytest
from tests.fixtures.fixtures import fixture_tm


class TestDeletion:

    @pytest.mark.usefixtures('tm')
    def test_dummy(self):
        assert True

    @pytest.mark.usefixtures('tm')
    def test_positive(self, tm):
        # Given il sistema è in idle e aspetta un comando utente
        # Then il task è rimosso correttamente
        # When l'utente cancella un task rimuovendolo dalla to-do list
        assert tm.delete(name_task='t1')

    @pytest.mark.usefixtures('tm')
    def test_negative(self, tm):
        # Given il sistema è in idle e aspetta un comando utente
        # When l'utente prova a cancellare un task non esistente nel sistema
        # Then il task non viene rimosso, si restituisce risultato negativo
        assert not tm.delete(name_task='some task that does not exist')
