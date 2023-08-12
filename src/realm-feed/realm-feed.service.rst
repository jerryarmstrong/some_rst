src/realm-feed/realm-feed.service.ts
====================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Injectable } from '@nestjs/common';

import { RealmProposalService } from '@src/realm-proposal/realm-proposal.service';

@Injectable()
export class RealmFeedService {
  constructor(private readonly realmProposalService: RealmProposalService) {}
}


