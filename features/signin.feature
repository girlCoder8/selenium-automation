Feature: Signin

    Scenario: Signedin Flow
        Given I navigate to Indeed site
        When I navigate to Signin Page
        Then I fill in account "test@indeedmail.com" and "1234567wW" to signin
        Then I can see "test@indeedmail.com" on Indeed portal
        Then Close Browser

#        Examples:
#            |   Row 1   |
#            |   Row 2   |
#            |   ...     |