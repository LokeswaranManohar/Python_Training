Feature: SwagLabs Web Browsing
  As a web surfer,
  I want to find products online,
  So I can but new things.

  Scenario Outline: Basic Login
    Given the SwagLabs home page is displayed
    When the user type "<username>"
    When the user type "<password>"
    When the user click login
    Then move and validate result page


    Examples:
      | username | password |
      | standard_user | secret_sauce|

    #Login with standard_user and validate home page add validation to result page
  # explore more on gherkin