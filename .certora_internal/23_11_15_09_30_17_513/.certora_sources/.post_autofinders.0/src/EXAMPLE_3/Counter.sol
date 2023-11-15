// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

error CoffeeBreak();

contract Counter {
   uint256 public number;

   function setNumber(uint256 newNumber, bool inLuck) public {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010000, 1037618708481) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010003, 5) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00016001, inLuck) }
       number = newNumber;
       if (newNumber == 0xC0FFEE && inLuck == true) {
           revert CoffeeBreak();
       }
   }
    
   function increment() public {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000000, 1037618708480) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000002, 0) }
        number++;
    }
}