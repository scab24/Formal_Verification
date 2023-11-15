// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

error CoffeeBreak();

contract Counter {
   uint256 public number;

   function setNumber(uint256 newNumber, bool inLuck) public {
       number = newNumber;
       if (newNumber == 0xC0FFEE && inLuck == true) {
           revert CoffeeBreak();
       }
   }
    
   function increment() public {
        number++;
    }
}