src/index.test.js
=================

Last edited: 2021-11-06 11:43:58

Contents:

.. code-block:: js

    const assert = require('assert');

const {
  fetchTokenPrices,
  fetchArweaveStorageCost,
  calculate,
  _setCacheMs,
  _promiseMap
} = require('./index');

const sleep = (ms) => {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
};

describe('fetchTokenPrices', () => {
  it('should work', async () => {
    const result = await fetchTokenPrices();
    assert(!!(result?.solana?.usd && result?.arweave?.usd), 'invalid fetchTokenPrices response');
  })
})

describe('fetchArweaveStorageCost', () => {
  it('should fail when bytes are not passed', async () => {
    assert.rejects(async () => {
      await fetchArweaveStorageCost();
    }, /Invalid argument: totalBytes/);
  })

  it('should work', async () => {
    const result = await fetchArweaveStorageCost(1);
    assert(result > 100, 'invalid fetchArweaveStorageCost response');
  })
})

describe('cache', () => {
  it('caches results for the configured milliseconds', async () => {
    _promiseMap.clear();

    {
      _setCacheMs(0)
      await fetchTokenPrices();
      await sleep(50);
      assert(_promiseMap.size === 0, 'value still cached');
    }

    {
      _setCacheMs(1000)
      await fetchTokenPrices();
      await sleep(20);
      assert(_promiseMap.size === 1, 'value not cached');
      await sleep(1200);
      assert(_promiseMap.size === 0, 'value still cached');
    }

  })
})

describe('calculate', () => {
  it('should fail when file sizes are not passed', async () => {
    assert.rejects(async () => {
      await calculate();
    }, /Invalid argument: fileSizes must be an array of integers/);

    assert.rejects(async () => {
      await calculate([]);
    }, /Invalid argument: fileSizes must be an array of integers/);

    assert.rejects(async () => {
      await calculate('nope');
    }, /Invalid argument: fileSizes must be an array of integers/);

    assert.rejects(async () => {
      await calculate(['fail']);
    }, /Invalid argument: fileSizes must be an array of integers/);

  })

  it('returns the estimated total cost to upload files of the given sizes', async () => {
    const fileSizes = [2000, 2022000];
    const result = await calculate(fileSizes);

    assert(result.arweave > 0, result.arweave);
    assert(result.solana > 0, result.solanaPrice);
    assert(result.arweavePrice > 0, result.arweavePrice);
    assert(result.solanaPrice > 0, result.solanaPrice);
    assert(result.exchangeRate > 0, result.exchangeRate);
    assert.strictEqual(result.totalBytes, fileSizes[0] + fileSizes[1]);
  })
})

