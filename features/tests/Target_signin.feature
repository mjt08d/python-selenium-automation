# Created by michaeltrisotto at 3/31/24
Feature: Sign in verification


  Scenario: Verify user can sign in once logged out
    Given Open Target homepage
    When Click the "Sign in" button on upper right of homepage and click the "Sign in" button on drop down menu
    Then Verify "Sign in" page opens

