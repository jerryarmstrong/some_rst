docs/06-deprecated/04-storefront/01-init-store.md
=================================================

Last edited: 2023-08-08 19:56:25

Contents:

.. code-block:: md

    # Init store

### Setting Up the Store ID

When opening a store for the first time you will be asked to connect your wallet. Click the **Connect** button and follow the steps to get connected.

Once connected, the store will first run some checks to see if you've already set up a store. After a minute or so, a welcome screen is presented with an **Init Store** button.

![Init store](/assets/storefront/installation/init-store.png#radius#shadow)

From the wallet dropdown (Phantom pictured below), select a network (mainnet for production, testnet or devnet for practice).

![Select network](/assets/storefront/installation/select-wallet.png#radius#shadow)

:::tip

Before proceeding, you must have some SOL on your wallet to be able to pay the Init Store transaction fee. In the case of using devnet or testnet you can airdrop SOL to yourself via [Sol Faucet](https://solfaucet.com/).

:::

Click the **Init Store** button. This starts the store initialization process by prompting you to approve a transaction from your wallet. After approval, your store initialization begins which may take 1-2 minutes.

![Approve transaction](/assets/storefront/installation/approve-transaction.png#radius#shadow)

After store initialization completes, you must save your new store addresses. In the **Store configuration** section on the store page click on the **Copy** button and paste in the `.env` file in `js/packages/web`.

![Save env](/assets/storefront/installation/save-env.png#radius#shadow)

![Set env](/assets/storefront/installation/set-env.png#radius#shadow)

Now restart your webserver (_Ctrl + C_ + `yarn start`) for the `.env` changes to take effect.



