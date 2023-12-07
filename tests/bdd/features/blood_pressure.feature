Feature: Blood pressure calculation

  Scenario: Regular blood pressure values
    Given I have bp values of 120 and 80
    When I calculate the blood pressure
    Then I should get Ideal blood pressure
