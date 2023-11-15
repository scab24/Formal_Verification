// SPDX-License-Identifier: AGPL-3.0
pragma solidity >=0.8.0 <0.9.0;

contract Vault {
    uint public totalAssets;
    uint public totalShares;

    function deposit(uint assets) public returns (uint shares) {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010000, 1037618708481) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010003, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00016000, assets) }
        shares = (assets * totalShares) / totalAssets;

        totalAssets += assets;
        totalShares += shares;
    }

    function mint(uint shares) public returns (uint assets) {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000000, 1037618708480) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000003, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00006000, shares) }
        assets = (shares * totalAssets) / totalShares; // buggy

        totalAssets += assets;
        totalShares += shares;
    }
}