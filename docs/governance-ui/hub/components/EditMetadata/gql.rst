hub/components/EditMetadata/gql.ts
==================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

import { PublicKey } from '@hub/types/decoders/PublicKey';
import { RealmCategory } from '@hub/types/decoders/RealmCategory';
import { RichTextDocument } from '@hub/types/decoders/RichTextDocument';
import { RoadmapItemStatus } from '@hub/types/decoders/RoadmapItemStatus';

export const getMetadata = gql`
  query getMetadata($urlId: String!) {
    realmByUrlId(urlId: $urlId) {
      amAdmin
      bannerImageUrl
      category
      discordUrl
      displayName
      githubUrl
      heading
      iconUrl
      instagramUrl
      linkedInUrl
      membersCount
      name
      publicKey
      shortDescription
      symbol
      twitterFollowerCount
      twitterHandle
      urlId
      websiteUrl
      about {
        content
        heading
      }
      documentation {
        title
        url
      }
      faq {
        answer
        clippedAnswer(charLimit: 200) {
          document
          isClipped
        }
        question
      }
      gallery {
        caption
        height
        width
        url
      }
      resources {
        content
        title
        url
      }
      roadmap {
        description
        items {
          date
          resource {
            content
            title
            url
          }
          status
          title
        }
      }
      team {
        avatar
        description
        linkedIn
        name
        role
        twitter
        twitterFollowerCount
      }
      token {
        mint
        symbol
      }
    }
  }
`;

export const saveMetadata = gql`
  mutation updateRealmMetadata($publicKey: PublicKey!, $realm: RealmInput!) {
    updateRealmMetadata(publicKey: $publicKey, realm: $realm) {
      amAdmin
      bannerImageUrl
      category
      discordUrl
      displayName
      githubUrl
      heading
      iconUrl
      instagramUrl
      linkedInUrl
      membersCount
      name
      publicKey
      shortDescription
      symbol
      twitterFollowerCount
      twitterHandle
      urlId
      websiteUrl
      about {
        content
        heading
      }
      documentation {
        title
        url
      }
      faq {
        answer
        clippedAnswer(charLimit: 200) {
          document
          isClipped
        }
        question
      }
      gallery {
        caption
        height
        width
        url
      }
      resources {
        content
        title
        url
      }
      roadmap {
        description
        items {
          date
          resource {
            content
            title
            url
          }
          status
          title
        }
      }
      team {
        avatar
        description
        linkedIn
        name
        role
        twitter
        twitterFollowerCount
      }
      token {
        mint
        symbol
      }
    }
  }
`;

const realm = IT.type({
  amAdmin: IT.boolean,
  bannerImageUrl: IT.union([IT.null, IT.string]),
  category: RealmCategory,
  discordUrl: IT.union([IT.null, IT.string]),
  displayName: IT.string,
  githubUrl: IT.union([IT.null, IT.string]),
  heading: IT.union([IT.null, RichTextDocument]),
  iconUrl: IT.union([IT.null, IT.string]),
  instagramUrl: IT.union([IT.null, IT.string]),
  linkedInUrl: IT.union([IT.null, IT.string]),
  membersCount: IT.number,
  name: IT.string,
  publicKey: PublicKey,
  shortDescription: IT.union([IT.null, IT.string]),
  symbol: IT.union([IT.null, IT.string]),
  twitterFollowerCount: IT.number,
  twitterHandle: IT.union([IT.null, IT.string]),
  websiteUrl: IT.union([IT.null, IT.string]),
  urlId: IT.string,
  about: IT.array(
    IT.type({
      content: RichTextDocument,
      heading: IT.union([IT.null, IT.string]),
    }),
  ),
  documentation: IT.union([
    IT.null,
    IT.type({
      title: IT.union([IT.null, IT.string]),
      url: IT.string,
    }),
  ]),
  faq: IT.array(
    IT.type({
      answer: RichTextDocument,
      clippedAnswer: IT.type({
        document: RichTextDocument,
        isClipped: IT.boolean,
      }),
      question: IT.string,
    }),
  ),
  gallery: IT.array(
    IT.type({
      caption: IT.union([IT.null, IT.string]),
      url: IT.string,
      height: IT.number,
      width: IT.number,
    }),
  ),
  resources: IT.array(
    IT.type({
      content: IT.union([IT.null, RichTextDocument]),
      title: IT.string,
      url: IT.string,
    }),
  ),
  roadmap: IT.type({
    description: IT.union([IT.null, RichTextDocument]),
    items: IT.array(
      IT.type({
        date: IT.union([IT.null, IT.number]),
        resource: IT.union([
          IT.null,
          IT.type({
            content: IT.union([IT.null, RichTextDocument]),
            title: IT.string,
            url: IT.string,
          }),
        ]),
        status: IT.union([IT.null, RoadmapItemStatus]),
        title: IT.string,
      }),
    ),
  }),
  team: IT.array(
    IT.type({
      avatar: IT.union([IT.null, IT.string]),
      description: IT.union([IT.null, RichTextDocument]),
      linkedIn: IT.union([IT.null, IT.string]),
      name: IT.string,
      role: IT.union([IT.null, IT.string]),
      twitter: IT.union([IT.null, IT.string]),
      twitterFollowerCount: IT.number,
    }),
  ),
  token: IT.union([
    IT.null,
    IT.type({
      mint: PublicKey,
      symbol: IT.string,
    }),
  ]),
});

export const getMetadataResp = IT.type({
  realmByUrlId: realm,
});

export const saveMetadataResp = IT.type({
  updateRealmMetadata: realm,
});


