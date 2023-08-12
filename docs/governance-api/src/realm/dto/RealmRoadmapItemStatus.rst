src/realm/dto/RealmRoadmapItemStatus.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { registerEnumType } from '@nestjs/graphql';

/**
 * A discriminant for differentiating the status of a roadmap item
 */
export enum RealmRoadmapItemStatus {
  Completed = 'Completed',
  Delayed = 'Delayed',
  InProgress = 'InProgress',
  Upcoming = 'Upcoming',
}

registerEnumType(RealmRoadmapItemStatus, {
  name: 'RealmRoadmapItemStatus',
  description: 'A discriminant for differentiating the status of a roadmap item',
});


