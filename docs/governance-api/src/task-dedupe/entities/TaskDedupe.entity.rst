src/task-dedupe/entities/TaskDedupe.entity.ts
=============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import {
  Column,
  CreateDateColumn,
  Entity,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
} from 'typeorm';

@Entity()
export class TaskDedupe {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({
    type: 'jsonb',
    nullable: true,
  })
  result?: any;

  @Column()
  key: string;

  @CreateDateColumn()
  created: Date;

  @UpdateDateColumn()
  updated: Date;
}


