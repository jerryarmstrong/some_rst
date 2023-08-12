src/realm-feed-item-comment/dto/pagination.ts
=============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, registerEnumType } from '@nestjs/graphql';

import { EdgeType, ConnectionType } from '@lib/gqlTypes/Connection';

import { RealmFeedItemComment } from './RealmFeedItemComment';

@ObjectType()
export class RealmFeedItemCommentEdge extends EdgeType(
  'RealmFeedItemComment',
  RealmFeedItemComment as any,
) {}

@ObjectType()
export class RealmFeedItemCommentConnection extends ConnectionType<RealmFeedItemCommentEdge>(
  'RealmFeedItemComment',
  RealmFeedItemCommentEdge,
) {}

export enum RealmFeedItemCommentSort {
  New = 'New',
  Relevance = 'Relevance',
  TopAllTime = 'TopAllTime',
}

registerEnumType(RealmFeedItemCommentSort, {
  name: 'RealmFeedItemCommentSort',
  description: 'Sort order for a list of comments',
});


