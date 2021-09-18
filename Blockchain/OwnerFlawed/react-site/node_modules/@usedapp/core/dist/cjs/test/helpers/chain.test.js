"use strict";
exports.__esModule = true;
var chai_1 = require("chai");
var src_1 = require("../../src");
var chain_1 = require("../../src/helpers/chain");
describe('Chain helpers', function () {
    it('getChainName', function () {
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Mainnet)).to.eq('Mainnet');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Ropsten)).to.eq('Ropsten');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Kovan)).to.eq('Kovan');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Rinkeby)).to.eq('Rinkeby');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Goerli)).to.eq('Goerli');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.BSC)).to.eq('BSC');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.xDai)).to.eq('xDai');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Polygon)).to.eq('Polygon');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Mumbai)).to.eq('Mumbai');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Harmony)).to.eq('Harmony');
        chai_1.expect(chain_1.getChainName(src_1.ChainId.Moonriver)).to.eq('Moonriver');
    });
    it('isTestChain', function () {
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Mainnet)).to.be["false"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Ropsten)).to.be["true"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Kovan)).to.be["true"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Rinkeby)).to.be["true"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Goerli)).to.be["true"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.BSC)).to.be["false"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.xDai)).to.be["false"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Polygon)).to.be["false"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Mumbai)).to.be["true"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Harmony)).to.be["false"];
        chai_1.expect(chain_1.isTestChain(src_1.ChainId.Moonriver)).to.be["false"];
    });
    it('isLocalChain', function () {
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Mainnet)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Ropsten)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Kovan)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Rinkeby)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Goerli)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.xDai)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Harmony)).to.be["false"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Localhost)).to.be["true"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Hardhat)).to.be["true"];
        chai_1.expect(chain_1.isLocalChain(src_1.ChainId.Moonriver)).to.be["false"];
    });
    it('getExplorerAddressLink', function () {
        var address = '0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987';
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Mainnet)).to.eq('https://etherscan.io/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Ropsten)).to.eq('https://ropsten.etherscan.io/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Kovan)).to.eq('https://kovan.etherscan.io/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Rinkeby)).to.eq('https://rinkeby.etherscan.io/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Goerli)).to.eq('https://goerli.etherscan.io/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.BSC)).to.eq('https://bscscan.com/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.xDai)).to.eq('https://blockscout.com/poa/xdai/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987/transactions');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Polygon)).to.eq('https://explorer-mainnet.maticvigil.com/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987/transactions');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Mumbai)).to.eq('https://explorer-mumbai.maticvigil.com/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987/transactions');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Harmony)).to.eq('https://explorer.harmony.one/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987');
        chai_1.expect(chain_1.getExplorerAddressLink(address, src_1.ChainId.Moonriver)).to.eq('https://blockscout.moonriver.moonbeam.network/address/0xC7095A52C403ee3625Ce8B9ae8e2e46083b81987/transactions');
    });
    it('getExplorerTransactionLink', function () {
        var tx = '0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a';
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Mainnet)).to.eq('https://etherscan.io/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Ropsten)).to.eq('https://ropsten.etherscan.io/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Kovan)).to.eq('https://kovan.etherscan.io/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Rinkeby)).to.eq('https://rinkeby.etherscan.io/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Goerli)).to.eq('https://goerli.etherscan.io/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.BSC)).to.eq('https://bscscan.com/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.xDai)).to.eq('https://blockscout.com/poa/xdai/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a/internal-transactions');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Polygon)).to.eq('https://explorer-mainnet.maticvigil.com/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a/internal-transactions');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Mumbai)).to.eq('https://explorer-mumbai.maticvigil.com/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a/internal-transactions');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Harmony)).to.eq('https://explorer.harmony.one/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a');
        chai_1.expect(chain_1.getExplorerTransactionLink(tx, src_1.ChainId.Moonriver)).to.eq('https://blockscout.moonriver.moonbeam.network/tx/0x5d53558791c9346d644d077354420f9a93600acf54eb6a279f12b43025392c3a/internal-transactions');
    });
});
//# sourceMappingURL=chain.test.js.map