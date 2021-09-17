import { Flex, Text, Button } from "@chakra-ui/react";
import { useCount } from "../hooks";
import { useEthers } from "@usedapp/core";

  

export default function Flag() {
    const {account, deactivate} = useEthers();
    const currentOwner = useCount();
    if(account!=currentOwner){
        return (
            <Flex direction="column" align="center" mt="4">
                <Text color="white" fontSize="2xl">
                    You are not {currentOwner}, the current owner
                </Text>
            </Flex>
        );
    }else if(account && account==currentOwner){
        return (
            <Flex direction="column" align="center" mt="4">
                <Text color="white" fontSize="2xl">
                    {process.env.REACT_APP_PBJAR_FLAG}
                </Text>
            </Flex>
        );
    }else{
        return (
            <Flex direction="column" align="center" mt="4">
                <Text color="white" fontSize="2xl">
                    Install Metamask to connect
                </Text>
            </Flex>
        );
    }
}