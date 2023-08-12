docs/01-programs/03-auction-house/06-auction-house-receipts.md
==============================================================

Last edited: 2023-08-08 19:56:25

Contents:

.. code-block:: md

    ---
description: "Explains how to generate Auction House receipts."
---

import { Accordion, AccordionItem } from '/src/accordion.jsx';

# Auction House Receipts

## Introduction

To aid transaction / activity tracking on marketplaces, the Auction House program supports the generation of receipts for listings, bids and sales.

In addition to printing receipts, Auction House cancels receipts when the corresponding instruction (bid, listing or sale) is cancelled.

Let us see how receipts are printed.

## Printing Receipts

To generate these receipts, the receipt printing function should be called immediately after the corresponding transaction (`PrintListingReceipt`, `PrintBidReceipt`, and `PrintPurchaseReceipt`).

Additionally, the `CancelListingReceipt `and `CancelBidReceipt` instructions should be called in the case of canceled listings and bids. Calling these two instructions will fill the `canceled_at` fields of the `ListingReceipt` and `BidReceipt` accounts.

> While the receipts can be retrieved using the standard getProgramAccounts data flow, the official recommendation is to use Solana's AccountsDB plug-in to index and track the generated receipts.

<Accordion>
<AccordionItem title="JS SDK" open={true}>
<div className="accordion-item-padding">

There are two fields that can be introduced to each function above to print the corresponding receipt:

1. `printReceipt`: This is a boolean field that defaults to `true`. When this field is set to `true`, a receipt is printed for the corresponding function.

2. `bookkeeper`: The address of the bookkeeper wallet responsible for the receipt. In other words, the bookeeper is the wallet that paid for the receipt. It's only responsibility at this time is tracking the payer of the receipt so that in the future if the account is allowed to be closed the program knows who should be refunded for the rent. This field defaults to `metaplex.identity()`.

Here's an example of printing receipts for bid, list and execute sale instructions.
     
```tsx
// printing the ListReceipt
await metaplex
    .auctionHouse()
    .createListing({
        printReceipt: true,
        bookkeeper: metaplex.identity()
    })

// printing the BidReceipt
await metaplex
    .auctionHouse()
    .createBid({
        printReceipt: true,
        bookkeeper: metaplex.identity()
    })

// printing the PurchaseReceipt
await metaplex
    .auctionHouse()
    .executeSale({
        printReceipt: true,
        bookkeeper: metaplex.identity()
    })
```

</div>
</AccordionItem>
</Accordion>

## Conclusion

Now that we know how to print receipts for easy transaction tracking, how do we actually fetch details regarding these actions in practice? Let us explore ways to find bids, listings and sales for an Auction House in the [next page](/programs/auction-house/finding-bids-listings-and-sales).


