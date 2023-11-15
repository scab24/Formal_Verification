// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "lib/forge-std/src/Test.sol";
import "src/EXAMPLE_3/Counter.sol";

contract CounterHalmosTest is Test {
    Counter public counter;

    function setUp() public {
        counter = new Counter();
    }

    function check_testIncrement() public {
        uint256 initialNumber = counter.number();
        counter.increment();
        assert(counter.number() == initialNumber + 1);
    }

    function check_testFSetNumber(uint256 x, bool inLuck) public {
        counter.setNumber(x, inLuck);
        assert(counter.number() == x);
    }

    function check_testSetNumber(uint256 x, bool inLuck) public {
        try counter.setNumber(x, inLuck) {
            // Check if the function should not reverse
            if (!(x == 0xC0FFEE && inLuck)) {
                assert(counter.number() == x);
            }
        } catch Error(string memory reason) {
            // Check if the function should revert
            assert(x == 0xC0FFEE && inLuck);
        }
    }

    function check_testSetNumberRevertsOnCondition() public {
        // Activates the revert
        try counter.setNumber(0xC0FFEE, true) {
            fail("Should revert with CoffeeBreak, but it didn't.");
        } catch Error(string memory reason) {
            // Confirm that the reason for revert is 'CoffeeBreak'.
            assertEq(reason, "CoffeeBreak");
        }
    }
}
