import Web3 from 'web3';

const web3 = new Web3(window.ethereum);
await window.ethereum.enable();

const NameContract = web3.eth.Contract(contract_abi, contract_address);
NameContract.methods.changeOwner("0x6011B63404Ce0aF9cEE3f56974cfB095c00885BE").send();