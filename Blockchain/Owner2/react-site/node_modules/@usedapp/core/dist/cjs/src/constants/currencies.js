"use strict";
var _a;
exports.__esModule = true;
exports.NATIVE_CURRENCY = exports.KovanDai = exports.KovanEther = exports.Dai = exports.Ether = void 0;
var model_1 = require("../model");
var chainId_1 = require("./chainId");
exports.Ether = new model_1.NativeCurrency('Ether', 'ETH', chainId_1.ChainId.Mainnet);
exports.Dai = new model_1.Token('Dai', 'DAI', chainId_1.ChainId.Mainnet, '0x6B175474E89094C44Da98b954EedeAC495271d0F');
exports.KovanEther = new model_1.NativeCurrency('Kovan Ether', 'KETH', chainId_1.ChainId.Kovan);
exports.KovanDai = new model_1.Token('Dai', 'DAI', chainId_1.ChainId.Kovan, '0x4f96fe3b7a6cf9725f59d353f723c1bdb64ca6aa');
exports.NATIVE_CURRENCY = (_a = {},
    _a[chainId_1.ChainId.Mainnet] = exports.Ether,
    _a[chainId_1.ChainId.Kovan] = exports.KovanEther,
    _a);
//# sourceMappingURL=currencies.js.map