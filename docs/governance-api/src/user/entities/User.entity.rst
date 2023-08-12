src/user/entities/User.entity.ts
================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  PrimaryGeneratedColumn,
  Unique,
  UpdateDateColumn,
  OneToMany,
} from 'typeorm';

import { RealmPost } from '@src/realm-post/entities/RealmPost.entity';

export interface Data {
  realmsFollowed?: string[];
}

@Entity()
@Unique(['authId'])
export class User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('jsonb')
  data: Data;

  @Column()
  authId: string;

  @Column()
  publicKeyStr: string;

  @OneToMany('RealmPost', 'author')
  posts: RealmPost[];

  @CreateDateColumn()
  created: Date;

  @DeleteDateColumn()
  deleted: Date;

  @UpdateDateColumn()
  updated: Date;
}


