README.md
=========

Last edited: 2021-11-06 11:43:58

Contents:

.. code-block:: md

    # Arweave cost

Calculates the cost of uploading files to [Arweave](https://arweave.org/) using [arbundles](https://github.com/Bundlr-Network/arbundles).

## Installation

```
npm i @metaplex/arweave-cost
```

## Use

```js
const { calculate } = require('@metaplex/arweave-cost');

const cost = await calculate([fileSizeInBytes0, fileSizeInBytes1, ...]);

console.log(`The cost to store the files is ${cost.solana} SOL or ${cost.arweave} AR`);
```

### Methods

#### calculate

Returns an object of storage cost information.

```js
const fileSizes = [2000, 32934]; // in bytes
const result = await calculate(fileSizes);
console.log(result)

// {
//   arweave: 0.0009903326292,         // The cost to store the files in AR
//   solana: 0.00025095896478276764,   // The cost in to store the files in SOL
//   arweavePrice: 52.41,              // Current AR price
//   solanaPrice: 206.82,              // Current SOL price
//   exchangeRate: 0.2534087612416594, // AR/SOL rate
//   totalBytes: 2024000,              // Total bytes calculated
//   byteCost: 861158808,              // Cost of storage in winstons without fees
//   fee: 129173821.19999999           // Total storage fees in winstons
// }
```

#### fetchArweaveStorageCost

Retreives the current storage cost (in Winstons) of a given number of `bytes` on
the Arweave network (without fees). Values are cached internally for 15 seconds.

```js
const arweaveCost = await fetchArweaveStorageCost(bytes);
console.log(arweaveCost); // 1798603
```

#### fetchPrices

Retreives the current price of AR and SOL from coingecko API. Values are cached
internally for 15 seconds.

```js
// Fetch the current arweave and solana prices
const rates = await fetchTokenPrices();
console.log(rates.solana.usd, rates.arweave.usd); // 206.4  52.29
```

## Development

### Running tests

```
npm test
```

### Debugging

This module uses the [debug](https://github.com/visionmedia/debug) module. To
enable debug logs, set the DEBUG environment variable:

```
DEBUG=arweave-cost npm test
```

