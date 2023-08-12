src/realm/dto/Realm.ts
======================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@lib/scalars/PublicKey';
import { RichTextDocumentScalar } from '@lib/scalars/RichTextDocument';
import { RichTextDocument } from '@lib/types/RichTextDocument';

import { RealmAboutSection } from './RealmAboutSection';
import { RealmCategory } from './RealmCategory';
import { RealmDocumentation } from './RealmDocumentation';
import { RealmFaqItem } from './RealmFaqItem';
import { RealmGalleryItem } from './RealmGalleryItem';
import { RealmResource } from './RealmResource';
import { RealmRoadmap } from './RealmRoadmap';
import { RealmTeamMember } from './RealmTeamMember';
import { RealmTokenDetails } from './RealmTokenDetails';

@ObjectType({
  description: 'A Realm',
})
export class Realm {
  @Field(() => [RealmAboutSection], {
    description: 'Long form text describing the Realm',
  })
  about: RealmAboutSection[];

  @Field({
    description: "Url for the Realm's banner",
    nullable: true,
  })
  bannerImageUrl?: string;

  @Field(() => RealmCategory, {
    description: 'Indicates what type of Realm this is',
  })
  category: RealmCategory;

  @Field({
    description: 'Discord link',
    nullable: true,
  })
  discordUrl?: string;

  @Field({
    description: 'The display name of the org',
  })
  displayName: string;

  @Field(() => RealmDocumentation, {
    description: 'Optional documentation for the Realm',
    nullable: true,
  })
  documentation?: RealmDocumentation;

  @Field(() => [RealmFaqItem], {
    description: 'Frequently asked questions in the Realm',
  })
  faq: RealmFaqItem[];

  @Field(() => [RealmGalleryItem], {
    description: 'A list of items in the gallery',
  })
  gallery: RealmGalleryItem[];

  @Field({
    description: 'Github link',
    nullable: true,
  })
  githubUrl?: string;

  @Field(() => RichTextDocumentScalar, {
    description: 'An optional tagline or heading for the Realm',
    nullable: true,
  })
  heading?: RichTextDocument;

  @Field({
    description: "Url for the Realm's icon",
    nullable: true,
  })
  iconUrl?: string;

  @Field({
    description: 'Instagram url',
    nullable: true,
  })
  instagramUrl?: string;

  @Field({
    description: 'LinkedIn url',
    nullable: true,
  })
  linkedInUrl?: string;

  @Field({
    description: 'Name of the Realm',
  })
  name: string;

  @Field(() => PublicKeyScalar, {
    description: 'Public key of the governance program the Realm uses',
    nullable: true,
  })
  programPublicKey?: PublicKey;

  @Field(() => PublicKeyScalar, {
    description: 'Public Key address for the Realm',
  })
  publicKey: PublicKey;

  @Field(() => [RealmResource], {
    description: 'A list of external resources relevant to the Realm',
  })
  resources: RealmResource[];

  @Field(() => RealmRoadmap, {
    description: 'A roadmap for the Realm',
  })
  roadmap: RealmRoadmap;

  @Field({
    description: 'A short text description of the Realm',
    nullable: true,
  })
  shortDescription?: string;

  @Field({
    description: 'Symbol for the Realm',
    nullable: true,
  })
  symbol?: string;

  @Field(() => [RealmTeamMember], {
    description: 'A list of highlighted team members',
  })
  team: RealmTeamMember[];

  @Field(() => RealmTokenDetails, {
    description: 'Optional associated token',
    nullable: true,
  })
  token?: RealmTokenDetails;

  @Field({
    description: 'Twitter handle for the Realm',
    nullable: true,
  })
  twitterHandle?: string;

  @Field({
    description: 'The url id representation of the realm',
  })
  urlId: string;

  @Field({
    description: 'Website url for the Realm',
    nullable: true,
  })
  websiteUrl?: string;
}


