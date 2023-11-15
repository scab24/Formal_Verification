// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "lib/forge-std/src/Test.sol";
import {Token} from "src/EXAMPLE_4/Token.sol";

contract hevmTokenTest is Test {
    Token token; // Contract under test

    address alice = vm.addr(1);
    address bob = vm.addr(2);
    address Eve = vm.addr(3);

    function setUp() public {
        token = new Token();
        token.mint(alice, 10 ether);
        token.mint(bob, 20 ether);
        token.mint(Eve, 30 ether);
    }

    function prove_Transfer(address from, address to, uint256 amount) public {
        vm.assume(token.balanceOf(from) >= amount);

        uint256 preBalanceFrom = token.balanceOf(from);
        uint256 preBalanceTo = token.balanceOf(to);

        vm.prank(from);
        token.transfer(to, amount);

        if(from == to) {
            assert(token.balanceOf(from) == preBalanceFrom);
            assert(token.balanceOf(to)== preBalanceTo);
        } else {
            assert(token.balanceOf(from) == preBalanceFrom - amount);
            assert(token.balanceOf(to) == preBalanceTo + amount);
        }
    }

}