// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

contract readFlag1 {
    string private flag = "flag{etherscan_S0urc3_c0de}";

    function get() public view returns (string memory) {
        return flag;
    }
}