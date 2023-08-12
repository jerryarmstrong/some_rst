src/discord-user/dto/DiscordInteractionPayload.ts
=================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, ObjectType } from '@nestjs/graphql';

class DiscordData {
  @Field()
  name: string;
}

@ObjectType({
  description: 'The Discord interaction payload',
})
export class DiscordInteractionPayload {
  @Field()
  type: number;

  @Field()
  data: DiscordData;
}


