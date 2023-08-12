src/index.ts
============

Last edited: 2021-11-06 11:43:58

Contents:

.. code-block:: ts

    const request = require('axios');
const debug = require('debug')('arweave-cost');

const assert = (truthy: any, msg: string) => {
  if (!truthy) throw new Error(msg);
};

// arbundler uses a pricing endpoint which also accurately captures L2 fees.
// https://node1.bundlr.network/price/{totalUploadedBytes}
// internal fee calculation: fee(n) = bundler fee * l1_fee(1) * max(n, 2048) * network difficulty multiplier

const ARWEAVE_URL = 'https://node1.bundlr.network';
const CONVERSION_RATES_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=solana,arweave&vs_currencies=usd';
const WINSTON_MULTIPLIER = 10 ** 12;

const toInt = (val: any): number => parseInt(val, 10);

type asyncFunction = (...args: any[]) => Promise<any>;

/**
 * Cache promise results for 30 seconds
 */
let promiseCacheMs = 30000;
export const _setCacheMs = (ms: number) => promiseCacheMs = ms;

export const _promiseMap = new Map();

const memoPromise = (method: asyncFunction, args: any[]) => {
  const key = `${method.toString()}${JSON.stringify(args)}`;

  if (_promiseMap.has(key)) {
    return _promiseMap.get(key);
  }

  const promise = new Promise(function (resolve, reject) {
    return method(...args).catch((err) => {
      _promiseMap.delete(method);
      reject(err);
    }).then(resolve);
  });

  // cache for the configured time
  _promiseMap.set(key, promise);

  const timer = setTimeout(() => {
    _promiseMap.delete(key);
  }, promiseCacheMs);

  // allow program exit while timer is active
  if (timer.unref) {
    timer.unref();
  }

  return promise;
};

const memoize = (asyncFn: asyncFunction) => {
  return (...args: any[]) => {
    const result = memoPromise(asyncFn, args);
    return result
  };
};

export const fetchTokenPrices = memoize(() => {
  return request(CONVERSION_RATES_URL).then((response: any) => {
    const body = response.data;
    if (!(body.arweave?.usd && body.solana?.usd)) {
      debug('Invalid coingecko response', body);
      throw new Error('Invalid response from coingecko');
    }

    return body;
  })
});

export const fetchArweaveStorageCost = memoize((totalBytes: number) => {
  assert(Number.isFinite(totalBytes), `Invalid argument: totalBytes. Received: ${totalBytes}`);
  return request(`${ARWEAVE_URL}/price/${totalBytes}`).then((response: { data: any }) => toInt(response.data));
});

const validate = (fileSizes: number[]): void => {
  assert(
    Array.isArray(fileSizes) && fileSizes.length > 0 && fileSizes.every((k) => {
      return Number(k) === k && !isNaN(k) && k >= 0 && isFinite(k);
    }),
    'Invalid argument: fileSizes must be an array of integers');
};

const kb = (kilobytes: number) => kilobytes * 1024;
const MINIMUM_WINSTON_FEE = 10000000; // 0.00001 AR
const AR_FEE_MULTIPLIER = 15 / 100; // 15%

// test this. Then make public. Then pull into arweave cloud fn and metaplex
export const calculate = async (
  fileSizes: number[]
): Promise<{
  solana: number,
  arweave: number,
  arweavePrice: number,
  solanaPrice: number,
  exchangeRate: number,
  totalBytes: number,
}> => {

  validate(fileSizes);

  const totalBytes = fileSizes.reduce((sum, fileSize) => {
    return sum += fileSize;
  }, 0);

  const [conversionRates, totalWinstonCost] = await Promise.all([
    fetchTokenPrices(),
    fetchArweaveStorageCost(totalBytes)
  ]);

  const totalArCost = totalWinstonCost / WINSTON_MULTIPLIER;

  const arweavePrice = conversionRates.arweave.usd;
  const solanaPrice = conversionRates.solana.usd;
  const exchangeRate = arweavePrice / solanaPrice;

  debug('%j', {
    arweaveRate: arweavePrice,
    solanaRate: solanaPrice,
    exchangeRate,
    WINSTON_MULTIPLIER,
    totalWinstonCost,
    totalArCost,
    totalBytes
  });

  return {
    arweave: totalArCost,
    solana: totalArCost * exchangeRate,
    arweavePrice,
    solanaPrice,
    exchangeRate,
    totalBytes,
  };
};


