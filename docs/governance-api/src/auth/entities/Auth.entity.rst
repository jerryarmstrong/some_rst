src/auth/entities/Auth.entity.ts
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
  UpdateDateColumn,
} from 'typeorm';

export interface Data {}

@Entity()
export class Auth {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('jsonb')
  data: Data;

  @Column()
  publicKeyStr: string;

  @CreateDateColumn()
  created: Date;

  @DeleteDateColumn()
  deleted: Date;

  @UpdateDateColumn()
  updated: Date;
}


