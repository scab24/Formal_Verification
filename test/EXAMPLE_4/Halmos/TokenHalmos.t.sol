// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "lib/forge-std/src/Test.sol";
import {SymTest} from "lib/halmos-cheatcodes/src/SymTest.sol";

import {Token} from "src/EXAMPLE_4/Token.sol";

contract HalmosTokenTest is SymTest,Test {
    Token token; // Contract under test

    address alice;
    address bob;
    address Eve;
    address owner;

    function setUp() public {

        alice = svm.createAddress("alice");
        bob = svm.createAddress("bob");
        Eve = svm.createAddress("Eve");
        owner = svm.createAddress("owner");

        uint256 Balancealice = svm.createUint256("Balancealice");
        uint256 Balancebob = svm.createUint256("Balancebob");
        uint256 Balanceeve = svm.createUint256("Balanceeve");
        uint256 Balanceowner = svm.createUint256("Balanceowner");


        vm.startPrank(owner);
        token = new Token();

        token.mint(alice, Balancealice);
        token.mint(bob, Balancebob);
        token.mint(Eve, Balanceeve);

        vm.stopPrank();

    }

    function check_Transfer(address from, address to, uint256 amount) public {
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