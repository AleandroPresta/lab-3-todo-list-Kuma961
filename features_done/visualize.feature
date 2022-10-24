Feature: visualizzazione dei task
  Scenario: l'utente visualizza i task esistenti
    Given il sistema è in idle e aspetta un comando utente
    When l'utente vuole visualizzare tutti i task
    Then i task vengono stampati a schermo
