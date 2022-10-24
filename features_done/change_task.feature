Feature: cambiamento dello stato di un task
  Scenario: l'utente cambia lo stato di un task (gli stati possibili sono DONE, TODO, DOING, WONTDO)
    Given il sistema è in idle e aspetta un comando utente
    When l'utente vuole cambiare lo stato di un task
    Then lo stato del task viene cambiato con successo
  Scenario: l'utente non riesce a cambiare lo stato di un task (gli stati possibili sono DONE, TODO, DOING, WONTDO)
    Given il sistema è in idle e aspetta un comando utente
    When l'utente vuole cambiare lo stato di un task ma inserisce uno stato che non è ammissibile
    Then lo stato del task non viene cambiato
