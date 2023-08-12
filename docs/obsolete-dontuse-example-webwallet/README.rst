README.md
=========

Last edited: 2020-08-30 15:21:22

Contents:

.. code-block:: md

    [![Build status][travis-image]][travis-url]

[travis-image]: https://api.travis-ci.org/solana-labs/example-webwallet.svg?branch=master
[travis-url]: https://travis-ci.org/solana-labs/example-webwallet

# Example Web Wallet

This project demonstrates how to use the [Solana Javascript API](https://github.com/solana-labs/solana-web3.js)
to implement a simple web wallet.

**IMPORTANT: This wallet does not sufficently protect the private keys it
generates and should NOT be used in a non-test environment**

## Getting Started

```
$ npm install
$ npm run start
```

Then open your browser to http://localhost:8080/

## Development

When making changes, using the webpack-dev-server can be quite convenient as it
will rebuild and reload the app automatically

```
$ npm run dev
```

## Funding dApps

If this wallet is opened by a dApp, it will accept requests for funds. In order to
request funds from your dApp, follow these steps:

1. Attach a message event listener to the dApp window
```js
window.addEventListener('message', (e) => { /* ... */ });
```
2. Open the wallet url in a window from the dApp
```js
const walletWindow = window.open(WALLET_URL, 'wallet', 'toolbar=no, location=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=500, height=600');
```
3. Wait for the wallet to load, it will post a `'ready'` message when it's ready to handle requests
```js
window.addEventListener('message', (e) => {
  if (e.data) {
    switch (e.data.method) {
      case 'ready': {
        // ...
        break;
      }
    }
  }
});
```
4. Send an `'addFunds'` request
```js
walletWindow.postMessage({
  method: 'addFunds',
  params: {
    pubkey: '7q4tpevKWZFSXszPfnvWDuuE19EhSnsAmt5x4MqCyyVb',
    amount: 150,
    network: 'https://devnet.solana.com',
  },
}, WALLET_URL);
```
5. Listen for an `'addFundsResponse'` event which will include the amount transferred and the transaction signature
```js
window.addEventListener('message', (e) => {
  // ...
  switch (e.data.method) {
    case 'ready': {
      // ...
      break;
    }
    case 'addFundsResponse': {
      const {amount, signature} = e.data.params;
      // ...
      break;
    }
  }
});
```


