src/realm-feed-item/dto/pagination.ts
=====================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, registerEnumType } from '@nestjs/graphql';

import { EdgeType, ConnectionType } from '@lib/gqlTypes/Connection';

import { RealmFeedItem } from './RealmFeedItem';

@ObjectType()
export class RealmFeedItemEdge extends EdgeType('RealmFeedItem', RealmFeedItem as any) {}

@ObjectType()
export class RealmFeedItemConnection extends ConnectionType<RealmFeedItemEdge>(
  'RealmFeedItem',
  RealmFeedItemEdge,
) {}

export enum RealmFeedItemSort {
  New = 'New',
  Relevance = 'Relevance',
  TopAllTime = 'TopAllTime',
}

registerEnumType(RealmFeedItemSort, {
  name: 'RealmFeedItemSort',
  description: 'Sort order for a list of Realm feed items',
});


