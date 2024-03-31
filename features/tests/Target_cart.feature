# Created by michaeltrisotto at 3/31/24
Feature: "Your cart is empty" text verification


  Scenario: Verity user can see "Your cart is empty" on "Cart" page
    Given Open Target homepage
    When Click on "Cart" icon
    Then Verify "Your cart is empty" text is shown