Feature: Running tests
  In order to prove that django-behave works
  As the maintainer
  I want to test running behave against this features directory

  Scenario: This test
    Given this step exists
    When I run "python manage.py behave"
    Then I should see the behave tests run


  Scenario: Test django_ready
    When I run "python manage.py behave"
    Then django_ready should be called
