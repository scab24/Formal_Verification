// SPDX-License-Identifier: AGPL-3.0
pragma solidity ^0.8.17;

import "lib/forge-std/src/Test.sol";
import "src/EXAMPLE_2/PostExample.sol";

contract HevmPostExampleTest is Test {
    PostExample public example;

    function setUp() public {
        example = new PostExample();
    }


      function prove_Backdoor(uint256 x) public view {
        example.backdoor(x);
        
    }
}