@logged_user @main_page @filter
Feature: Question search
  After user logged in to application he is able to manipulate data on the main page

  @main_page_1
  Scenario: Questions list presenting
    Given I login to application with correct credentials
    And Main Page is downloaded successfully
    When I filter questions by following parameters
        | filter        | value                      |
        | subject       | second subject in the list |
        | grade_level   | second grade in dropdown   |
        | answer_status | answered                   |
      And I click first filtered question
    Then question page is presented
      And question has correct subject and education_level parameter
      And at least one answer is presented on the page
