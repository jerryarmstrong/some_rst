src/auth/entities/AuthClaim.entity.ts
=====================================

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

@Entity()
export class AuthClaim {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  nonce: string;

  @Column()
  onBehalfOf: string;

  @CreateDateColumn()
  created: Date;

  @DeleteDateColumn()
  deleted: Date;

  @UpdateDateColumn()
  updated: Date;
}


