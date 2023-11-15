// SPDX-License-Identifier: AGPL-3.0
pragma solidity >=0.8.0 <0.9.0;

import "lib/forge-std/src/Test.sol";

import {Vault} from "src/EXAMPLE_1/Vault.sol";

contract VaultMock2 is Vault {
    function setTotalAssets(uint _totalAssets) public {
        totalAssets = _totalAssets;
    }

    function setTotalShares(uint _totalShares) public {
        totalShares = _totalShares;
    }
}

/// @custom:hevm test --match VaultHevmTest
contract VaultHevmTest is Test {
    VaultMock2 vault;

    function setUp() public {
        vault = new VaultMock2();

        uint256 totalAssetsValue = 123;
        uint256 totalSharesValue = 456; 

        vault.setTotalAssets(totalAssetsValue);
        vault.setTotalShares(totalSharesValue);
    }
    function prove_deposit(uint assets) public {
        uint A1 = vault.totalAssets();
        uint S1 = vault.totalShares();

        vault.deposit(assets);

        uint A2 = vault.totalAssets();
        uint S2 = vault.totalShares();

        // assert(A1 / S1 <= A2 / S2);
        assert(A1 * S2 <= A2 * S1); 
    }

    function prove_mint(uint shares) public {
        uint A1 = vault.totalAssets();
        uint S1 = vault.totalShares();

        vault.mint(shares);

        uint A2 = vault.totalAssets();
        uint S2 = vault.totalShares();

        // assert(A1 / S1 <= A2 / S2);
        assert(A1 * S2 <= A2 * S1);
    }
}