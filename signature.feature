Feature: Signature

  Scenario: Signature
    Given I login as admin user
    When I create an inspection
    And I click on camera button in 'Punch Item/Deficiency:' checkpoint on inspection page
    And I select 'Signature' option in camera dropdown on inspection page
    Then I should see drawing board
    When I draw signature on drawing board
    And I click on 'Save' button on drawing board
    Then I should see attached file to 'Punch Item/Deficiency:' checkpoint on inspection page
    When I click on 'Save' button on inspection page
    Then I should see 'Synced to server' inspection status
