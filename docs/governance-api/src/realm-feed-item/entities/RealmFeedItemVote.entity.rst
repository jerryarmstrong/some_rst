src/realm-feed-item/entities/RealmFeedItemVote.entity.ts
========================================================

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

import { RealmFeedItemVoteType } from '../dto/RealmFeedItemVoteType';

export interface Data {
  type: RealmFeedItemVoteType;
  relevanceWeight: number;
}

@Entity()
export class RealmFeedItemVote {
  @PrimaryColumn()
  feedItemId: number;

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


