hub/types/decoders/FeedItemType.ts
==================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';

import { FeedItemType as _FeedItemType } from '../FeedItemType';

export const FeedItemTypePost = IT.literal(_FeedItemType.Post);
export const FeedItemTypeProposal = IT.literal(_FeedItemType.Proposal);

export const FeedItemType = IT.union([FeedItemTypePost, FeedItemTypeProposal]);


