import { ethers } from "ethers";
import { useContractCall } from "@usedapp/core";
import simpleContractAbi from "../abi/simpleContractAddress.json";
import { simpleContractAddress } from "../contracts"

const simpleContractInterface = new ethers.utils.Interface(simpleContractAbi);

export function useCount() {
  const [count]: any = useContractCall({
    abi: simpleContractInterface,
    address: simpleContractAddress,
    method: "getCurrentOwner",
    args: [],
  }) ?? [];
  return count;
}