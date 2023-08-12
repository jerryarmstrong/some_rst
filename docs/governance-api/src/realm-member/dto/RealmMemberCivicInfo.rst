src/realm-member/dto/RealmMemberCivicInfo.ts
============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';

@ObjectType({
  description: 'Connected Civic info',
})
export class RealmMemberCivicInfo {
  @Field(() => String, {
    description: 'URL for the associated Civic avatar',
    nullable: true,
  })
  avatarUrl: string;

  @Field(() => String, {
    description: "User's civic handle",
  })
  handle: string;

  @Field(() => Boolean, {
    description: 'Whether the user been verified by civic',
  })
  isVerified: boolean;
}


