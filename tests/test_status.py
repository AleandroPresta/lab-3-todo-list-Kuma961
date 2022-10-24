import pytest
from tests.fixtures.fixtures import fixture_tm


class TestStatus:

    @pytest.mark.usefixtures('tm')
    def test_dummy(self):
        assert True

    @pytest.mark.usefixtures('tm')
    def test_change_positive(self, tm):
        # Given il sistema è in idle e aspetta un comando utente
        # When l'utente vuole cambiare lo stato di un task
        new_status = 'DOING'
        name_task = 't1'
        # Then lo stato del task viene cambiato con successo
        assert tm.change_status(name_task=name_task, new_status=new_status) is True

    @pytest.mark.usefixtures('tm')
    def test_change_negative_status(self, tm):
        # Given il sistema è in idle e aspetta un comando utente
        # When l'utente vuole cambiare lo stato di un task ma inserisce uno stato che non è ammissibile
        new_status = 'NOT DONE'
        name_task = 't1'
        # Then lo stato del task non viene cambiato con successo
        assert not tm.change_status(name_task=name_task, new_status=new_status)

    @pytest.mark.usefixtures('tm')
    def test_change_negative_name(self, tm):
        # Given il sistema è in idle e aspetta un comando utente
        # When l'utente vuole cambiare lo stato di un task che non esiste
        new_status = 'DOING'
        name_task = 'some task that does not exist'
        # Then lo stato del task non viene cambiato con successo
        assert not tm.change_status(name_task=name_task, new_status=new_status)


