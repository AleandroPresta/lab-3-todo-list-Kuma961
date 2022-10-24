Feature: creazione di un task
  Scenario: l'utente crea un task inserendo i parametri
    Given il sistema è in idle e aspetta un comando utente
    When l'utente crea un task e lo aggiunge alla to-do list
    Then il task è aggiunto correttamente