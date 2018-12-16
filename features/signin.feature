Feature: Signin

    Scenario: Signedin Flow
        Given I navigate to Indeed site
        When I navigate to Signin Page
        Then I fill in account "weigotest@protonmail.com" and "1234567wW" to signin
        Then I can see "weigotest@protonmail.com" on Indeed portal
        Then Close Browser

#        Examples:
#            |   Row 1   |
#            |   Row 2   |
#            |   ...     |