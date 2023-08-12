src/discord-user/dto/RefreshMetadata.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';

@ObjectType({
  description: 'Status of refreshing the Discord metadata',
})
export class RefreshMetadata {
  @Field({ description: 'Status of the refresh' })
  status: string;
}


