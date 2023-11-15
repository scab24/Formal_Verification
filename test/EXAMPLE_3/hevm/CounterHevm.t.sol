// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "lib/forge-std/src/Test.sol";
import "src/EXAMPLE_3/Counter.sol";

contract CounterHevmTest is Test {
   Counter public counter;

   function setUp() public {
       counter = new Counter();
       counter.setNumber(0, false);
   }

   function prove_testIncrement() public {
        counter.increment();
        assert(counter.number() == 1);
    }

   function prove_testSetNumber(uint256 x, bool inLuck) public {
       counter.setNumber(x, inLuck);
       assert(counter.number() == x);
   }

    function prove_Number(uint256 x, bool inLuck) public {
        try counter.setNumber(x, inLuck) {
            // Verifica si la función no debería revertir
            if (!(x == 0xC0FFEE && inLuck)) {
                assert(counter.number() == x);
            }
        } catch Error(string memory reason) {
            // Verifica si la función debería revertir
            assert(x == 0xC0FFEE && inLuck);
        }
    }
}