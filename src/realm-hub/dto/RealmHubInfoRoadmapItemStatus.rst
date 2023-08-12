src/realm-hub/dto/RealmHubInfoRoadmapItemStatus.ts
==================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { registerEnumType } from '@nestjs/graphql';

/**
 * A discriminant for differentiating the status of a roadmap item
 */
export enum RealmHubInfoRoadmapItemStatus {
  Completed = 'Completed',
  Delayed = 'Delayed',
  InProgress = 'InProgress',
  Upcoming = 'Upcoming',
}

registerEnumType(RealmHubInfoRoadmapItemStatus, {
  name: 'RealmHubInfoRoadmapItemStatus',
  description: 'A discriminant for differentiating the status of a roadmap item',
});


