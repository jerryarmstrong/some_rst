src/realm-feed-item-comment/entities/RealmFeedItemCommentVote.entity.ts
=======================================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  PrimaryColumn,
  UpdateDateColumn,
} from 'typeorm';

import { RealmFeedItemCommentVoteType } from '../dto/RealmFeedItemCommentVoteType';

export interface Data {
  type: RealmFeedItemCommentVoteType;
  relevanceWeight: number;
}

@Entity()
export class RealmFeedItemCommentVote {
  @PrimaryColumn()
  commentId: number;

  @PrimaryColumn('uuid')
  userId: string;

  @PrimaryColumn()
  realmPublicKeyStr: string;

  @Column('jsonb')
  data: Data;

  @CreateDateColumn()
  created: Date;

  @DeleteDateColumn()
  deleted: Date;

  @UpdateDateColumn()
  updated: Date;
}


