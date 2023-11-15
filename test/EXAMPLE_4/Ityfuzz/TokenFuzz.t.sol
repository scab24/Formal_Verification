// // SPDX-License-Identifier: UNLICENSED
// pragma solidity ^0.8.15;

// import "../../../solidity_utils/lib.sol";

// contract Token {
//     address immutable owner;
//     mapping(address => uint256) public balanceOf;

//     constructor() {
//         owner = msg.sender;
//     }

//     function mint(address user, uint256 amount) external {
//         require(msg.sender == owner, "Only owner can mint");
//         balanceOf[user] += amount;
//         bug();
//     }

//     function transfer(address to, uint amount) external {
//         balanceOf[msg.sender] -= amount;
//         balanceOf[to] += amount;
//         bug();
//     }

// }