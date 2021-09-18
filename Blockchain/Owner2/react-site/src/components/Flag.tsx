import { Flex, Text, Button } from "@chakra-ui/react";
import { useCount } from "../hooks/index";
import { useEthers } from "@usedapp/core";
import React from 'react'
import {useQuery} from 'react-query'
import axios from 'axios'

async function fetchPosts(){
    const {data} = await axios.get('http://localhost:3000')    
    return data
}

export default function Flag() {
    const {data, error, isError, isLoading } = useQuery('posts', fetchPosts)
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
                    {data}
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