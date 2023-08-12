docs/01-programs/03-auction-house/05-managing-buyer-account.md
==============================================================

Last edited: 2023-08-08 19:56:25

Contents:

.. code-block:: md

    ---
description: "Explains how to manage Buyer Escrow Accounts."
---

import { Accordion, AccordionItem } from '/src/accordion.jsx';

# Managing Buyer Escrow Account

## Introduction

In the previous page we discussed how to make bids and listings, and execute sales of assets. When we talked about execution of sales, we briefly mentioned the **Buyer Escrow Account**. What is the utility of this account and why do we need to talk about it?

This account is a program derived address (PDA) that acts as an escrow, by temporarily holds the bidder's funds (SOL or SPL-tokens). These funds are equal to the bidding price and are stored in this PDA until the sale goes through. When the sale is executed, the Auction House transfers these funds from the buyer escrow account PDA to the seller's wallet.

Now the question is: are these funds automatically transferred from the bidder's wallet to the buyer escrow account when the bid is made?

The answer is no. That is the very reason why we need to talk about managing the buyer escrow account and the funds in them. These funds are managed by the Auction House authority. Let us see how we the authority manages this account.

## Getting Balance

Adding to the discussion in the previous section, it is the responsibility of the Auction House to make sure that there are enough funds in the buyer escrow account, for the sale to go through. 

To do so, firstly the Auction House should know how much funds are currently there in the buyer escrow account.

<Accordion>
<AccordionItem title="JS SDK" open={true}>
<div className="accordion-item-padding">

Here's a code snippet that fetches the balance of the buyer escrow account for a given Auction House.

```tsx
import { Keypair } from "@solana/web3.js";

const buyerBalance = await metaplex
    .auctionHouse()
    .getBuyerBalance({
        auctionHouse,
        buyerAddress: Keypair.generate() // The buyer's address
    });
```

</div>
</AccordionItem>
</Accordion>

## Deposit Funds

At this point, the Auction House knows how much funds are currently there in the buyer escrow account corresponding to a user.

Now if this user makes a bid on an asset, Auction House can decide to transfer funds from the user's wallet to the buyer escrow account in case of insufficient funds.

<Accordion>
<AccordionItem title="JS SDK" open={true}>
<div className="accordion-item-padding">

Let us see how funds can be transferred from the buyer's wallet to the buyer escrow account for an Auction House.

```tsx
import { Keypair } from "@solana/web3.js";

const depositResponse = await metaplex
    .auctionHouse()
    .depositToBuyerAccount({
        auctionHouse,              // The Auction House in which escrow
                                   // buyer deposits funds. We only need a subset of
                                   // the `AuctionHouse` model but we need
                                   // enough information regarding its
                                   // settings to know how to deposit funds.
        buyer: metaplex.identity() // The buyer who deposits funds. This expects a Signer
        amount: 10                 // Amount of funds to deposit. This can either
                                   // be in SOL or in the SPL token used by
                                   // the Auction House as a currency.
    });
```

</div>
</AccordionItem>
</Accordion>

## Withdraw Funds

The Auction House should also be able to withdraw funds back from the buyer escrow wallet to the buyer's wallet, in case the user wants their funds back and / or have cancelled their bid.

<Accordion>
<AccordionItem title="JS SDK" open={true}>
<div className="accordion-item-padding">

Let us see how funds can be withdrawn from the buyer escrow wallet to the buyer's wallet for the given Auction House.

```tsx
import { Keypair } from "@solana/web3.js";

const withdrawResponse = await metaplex
    .auctionHouse()
    .withdrawFromBuyerAccount({
        auctionHouse,              // The Auction House from which escrow buyer withdraws funds
        buyer: metaplex.identity() // The buyer who withdraws funds
        amount: 10                 // Amount of funds to withdraw. This can either
                                   // be in SOL or in the SPL token used by
                                   // the Auction House as a currency.
    });
```

</div>
</AccordionItem>
</Accordion>

## Conclusion

Now that we have also discussed how to manage the funds in the buyer escrow account, we are very close to be able to fully launch and control our own marketplace.

One important piece of information currently missing: how does a marketplace keep track of the listings, bids and sales? The Auction House program has something in the store for doing this, namely [Receipts](/programs/auction-house/auction-house-receipts).


