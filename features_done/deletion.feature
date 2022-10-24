Feature: creazione di un task
  Scenario: l'utente cancella un task esistente dal sistema
    Given il sistema è in idle e aspetta un comando utente
    When l'utente cancella un task rimuovendolo dalla to-do list
    Then il task è rimosso correttamente

  Scenario: l'utente cancella un task non esistente dal sistema
    Given il sistema è in idle e aspetta un comando utente
    When l'utente prova a cancellare un task non esistente nel sistema
    Then il task non viene rimosso, si restituisce risultato negativo