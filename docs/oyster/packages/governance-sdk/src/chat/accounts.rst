packages/governance-sdk/src/chat/accounts.ts
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import BN from 'bn.js';

export const GOVERNANCE_CHAT_PROGRAM_ID = new PublicKey(
  'gCHAtYKrUUktTVzE4hEnZdLV4LXrdBf6Hh9qMaJALET',
);

export enum GovernanceChatAccountType {
  Uninitialized = 0,
  ChatMessage = 1,
}

export interface GovernanceChatAccount {
  accountType: GovernanceChatAccountType;
}

export type GovernanceChatAccountClass = typeof ChatMessage;

export enum ChatMessageBodyType {
  Text = 0,
  Reaction = 1,
}

export class ChatMessageBody {
  type: ChatMessageBodyType;
  value: string;
  isReply: boolean;

  constructor(args: {
    type: ChatMessageBodyType;
    value: string;
    isReply?: boolean;
  }) {
    this.type = args.type;
    this.value = args.value;
    this.isReply = args.isReply ?? false;
  }
}

export class ChatMessage {
  accountType = GovernanceChatAccountType.ChatMessage;

  proposal: PublicKey;
  author: PublicKey;
  postedAt: BN;
  replyTo: PublicKey | undefined;
  body: ChatMessageBody;

  constructor(args: {
    proposal: PublicKey;
    author: PublicKey;
    postedAt: BN;
    replyTo: PublicKey | undefined;
    body: ChatMessageBody;
  }) {
    this.proposal = args.proposal;
    this.author = args.author;
    this.postedAt = args.postedAt;
    this.replyTo = args.replyTo;
    this.body = args.body;
  }
}


