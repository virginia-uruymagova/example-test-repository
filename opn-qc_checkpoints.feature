Feature: OPN/QC Checkpoints

  @WIP
  Scenario: OPN/QC checkpoints work as expected
    Given I login as admin user
    When I create an inspection via 'CT150'
    When I click on 'OPN' checkbox in 'Quality Checkpoint' checkpoint on inspection page
    When I fill 'Corrective Action Notes' field for 'Quality Checkpoint' checkpoint with 'actionNote'
    And I fill 'Responsible Party' field for 'Quality Checkpoint' checkpoint with 'Responsible Party 2 (V1)'
    Then I should see 'Synced to server' inspection status
    When I click on 'FTQ' checkbox in 'Quality Checkpoint' checkpoint on inspection page
    And I refresh page
    And I click on 'OPN' checkbox in 'Quality Checkpoint' checkpoint on inspection page
    Then I should see changes made to fields in 'Quality Checkpoint' checkpoint on inspection page