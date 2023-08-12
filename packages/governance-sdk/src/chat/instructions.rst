packages/governance-sdk/src/chat/instructions.ts
================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { ChatMessageBody } from './accounts';

export enum GovernanceChatInstruction {
  PostMessage = 0,
}

export class PostChatMessageArgs {
  instruction: GovernanceChatInstruction =
    GovernanceChatInstruction.PostMessage;
  body: ChatMessageBody;

  constructor(args: { body: ChatMessageBody }) {
    this.body = args.body;
  }
}


