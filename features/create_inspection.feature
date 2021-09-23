Feature: Create Inspection

  Scenario: Create Inspection
    Given I login as admin user
    And I navigate to create inspection page
    Then I should wait until 'Loading data' modal will be closed
    When I select 'CT147' checklist on create inspection page
    And I select 'V1' vendor on create inspection page
    Then inspection is created successfully
    When I click on 'Save' button on inspection page
    Then I wait until Inspection ID value appears on inspection page
