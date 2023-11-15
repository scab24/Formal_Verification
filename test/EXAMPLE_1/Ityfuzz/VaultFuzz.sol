// // SPDX-License-Identifier: UNLICENSED
// pragma solidity ^0.8.15;

// import "../../../solidity_utils/lib.sol";

// contract Vault {
//     uint public totalAssets;
//     uint public totalShares;

//     function deposit(uint assets) public returns (uint shares) {
//         shares = (assets * totalShares) / totalAssets;

//         totalAssets += assets;
//         totalShares += shares;
    
//     }

//     function mint(uint shares) public returns (uint assets) {
//         assets = (shares * totalAssets) / totalShares; // buggy

//         totalAssets += assets;
//         totalShares += shares;
//         bug();
//     }
// }