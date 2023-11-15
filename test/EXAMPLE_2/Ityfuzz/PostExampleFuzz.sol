// // SPDX-License-Identifier: UNLICENSED
// pragma solidity ^0.8.15;

// import "../../../solidity_utils/lib.sol";

// contract PostExample {
//     // https://github.com/foundry-rs/foundry/issues/2851
//     function backdoor(uint256 x) external  {
//         uint256 number = 99;
//         unchecked {
//             uint256 z = x - 1;
//             if (z == 6912213124124531) {
//                 number = 0;
//             } else {
//                 number = 1;
//             }

//             // Insert bug() here to test the logic before the assertion
//         }
//             bug();
//         assert(number != 0);
//     }
// }