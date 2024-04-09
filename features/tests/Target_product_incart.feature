# Created by michaeltrisotto at 4/8/24
Feature: Verify item was added to cart


  Scenario: Verify cups were added to cart
    Given Open Target homepage
    When Click on the "Search" field and type in cups
    And Click Add to cart button
    And Click on "Add to cart" button from "Choose options" drop down
    And Click on "View cart & check out" button on dropdown menu
    Then Verify cups are in the cart