Feature: Emergency Dictionary Refresh

    Scenario: Emergency Dictionary Refresh
        Given I login as admin user
        And I navigate to Create Inspection page
        When I click on emergency dictionary refresh button
        Then I should see 'Loading data' modal
        And I should wait until 'Loading data' modal will be closed