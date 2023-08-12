src/realm-post/entities/RealmPost.entity.ts
===========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
  ManyToOne,
} from 'typeorm';

import { Environment } from '@lib/types/Environment';
import { RichTextDocument } from '@lib/types/RichTextDocument';
import { User } from '@src/user/entities/User.entity';

export interface Data {
  document: RichTextDocument;
  title: string;
}

@Entity()
export class RealmPost {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  authorId: string;

  @Column('jsonb')
  data: Data;

  @Column('varchar')
  environment: Environment;

  @Column()
  realmPublicKeyStr: string;

  @ManyToOne('User', 'posts')
  author: User;

  @CreateDateColumn()
  created: Date;

  @DeleteDateColumn()
  deleted: Date;

  @UpdateDateColumn()
  updated: Date;
}


