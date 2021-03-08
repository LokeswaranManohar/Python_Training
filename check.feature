Feature: SwagLabs Web Browsing
  As a web surfer,
  I want to find products online,
  So I can add to cart and buy it.



  Scenario Outline: Basic check
    Given the SwagLabs home page is displayed
    When the user type "<username>"
    When the user type "<password>"
    When the user click login
    Then in result page click on random item
    And move to cart page
    And click on checkout

    Examples:
      | username | password |
      | standard_user | secret_sauce|

    #Login with standard_user, add random item to card, navigate to cart, checkout


