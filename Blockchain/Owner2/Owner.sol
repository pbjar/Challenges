// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract Unprotected{
    address private owner;

    function changeOwner(address _newOwner) 
        public
    {
       owner = _newOwner;
    }
    
    function getCurrentOwner() public view returns (address) {
        return owner;
    }

}