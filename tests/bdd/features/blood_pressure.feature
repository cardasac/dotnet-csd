Feature: Blood pressure calculation

  Scenario: Regular blood pressure values
    Given I have bp values of 120 and 80
    When I calculate the blood pressure
    Then I should get Ideal blood pressure

  Scenario: Low blood pressure values
    Given I have bp values of 80 and 40
    When I calculate the blood pressure
    Then I should get Low blood pressure

  Scenario: PreHigh blood pressure values
    Given I have bp values of 140 and 90
    When I calculate the blood pressure
    Then I should get PreHigh blood pressure

  Scenario: High blood pressure values
    Given I have bp values of 180 and 90
    When I calculate the blood pressure
    Then I should get High blood pressure