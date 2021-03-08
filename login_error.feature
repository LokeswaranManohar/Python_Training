Feature: SwagLabs Web Browsing
  In SwagLabs Application,
  I try to give a locked user credentials,
  So I can see an error message.

  Scenario Outline: Basic DuckDuckGo API Query
    Given the SwagLabs home page is displayed
    When the user type "<username>"
    When the user type "<password>"
    When the user click login
    Then validate the error message

    Examples:
      | username | password |
      | locked_out_user| secret_sauce|

