Feature: Forgot Password

  @p1
  Scenario: Forgot Password
    Given I navigate to FTQ360 app
    When I click on 'Forgot password' link under Login form
    And I type 'dantheman5454' in 'User name' field
    And I click on 'Reset' button in Forgot Password form
    Then I should see in forgot password form following text:
      """
      We just sent a password reset email.
      When you receive the email, click on the link inside to reset your password.
      If you don't see the email after a few minutes, check spam folder.
      """
