src/realm-feed-item/dto/RealmFeedItemType.ts
============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { registerEnumType } from '@nestjs/graphql';

/**
 * A discriminant for differentiating between Realm Feed items
 */
export enum RealmFeedItemType {
  Post = 'Post',
  Proposal = 'Proposal',
}

registerEnumType(RealmFeedItemType, {
  name: 'RealmFeedItemType',
  description: 'A discriminant for differentiating between Realm Feed items',
  valuesMap: {
    [RealmFeedItemType.Post]: {
      description: 'A post feed item',
    },
    [RealmFeedItemType.Proposal]: {
      description: 'A proposal feed item',
    },
  },
});


