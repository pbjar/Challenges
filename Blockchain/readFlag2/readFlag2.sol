// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

contract readFlag2 {
    string private flag = "flag{web3js_plus_ABI_equalls_flag}";

    function get() public view returns (string memory) {
        return flag;
    }
}