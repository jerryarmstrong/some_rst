src/task-dedupe/task-dedupe.module.ts
=====================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { CacheModule, Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { TaskDedupe } from './entities/TaskDedupe.entity';
import { TaskDedupeService } from './task-dedupe.service';

@Module({
  imports: [CacheModule.register(), TypeOrmModule.forFeature([TaskDedupe])],
  providers: [TaskDedupeService],
  exports: [TaskDedupeService],
})
export class TaskDedupeModule {}


