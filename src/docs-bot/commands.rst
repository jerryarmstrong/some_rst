src/docs-bot/commands.ts
========================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { CommandInteraction } from 'discord.js';
import { CommandObject } from '../types';
import { algoliaResult, metaplexIndex, solanaIndex } from './handle-autocomplete';
import { wtfIs } from './wtf-is';

const slashCommands: CommandObject[] = [
    {
        data: {
            name: 'docs',
            description: 'Fetches the Metaplex Docs',
            defaultPermission: true,
            options: [
                {
                    name: 'query',
                    description: 'Phrase to search for',
                    type: 3,
                    required: true,
                    autocomplete: true,
                },
                {
                    name: 'target',
                    description: 'User to mention',
                    type: 6,
                    required: false,
                },
                {
                    name: 'hidden',
                    description: 'Only show the docs to you',
                    type: 5,
                    required: false,
                },
            ],
        },
        async execute(interaction: CommandInteraction) {
            await algoliaResult(metaplexIndex, interaction);
        },
        permissions: { modOnly: false },
    },
    {
        data: {
            name: 'soldocs',
            description: 'Fetches the Solana Docs',
            defaultPermission: true,
            options: [
                {
                    name: 'query',
                    description: 'Phrase to search for',
                    type: 3,
                    required: true,
                    autocomplete: true,
                },
                {
                    name: 'target',
                    description: 'User to mention',
                    type: 6,
                    required: false,
                },
                {
                    name: 'hidden',
                    description: 'Only show the docs to you',
                    type: 5,
                    required: false,
                },
            ],
        },
        async execute(interaction: CommandInteraction) {
            await algoliaResult(solanaIndex, interaction);
        },
        permissions: { modOnly: false },
    },
    {
        data: {
            name: 'wtf-is',
            description: 'What specific Metaplex errors mean! Uses the metaboss Rust crate under the hood.',
            defaultPermission: true,
            options: [
                {
                    name: 'code',
                    description: 'The hex code to look for',
                    type: 3,
                    required: true,
                },
                {
                    name: 'hidden',
                    description: 'Only show the error message to you',
                    type: 5,
                    required: false,
                },
            ],
        },
        async execute(interaction: CommandInteraction) {
            await wtfIs(interaction);
        },
        permissions: { modOnly: false },
    },
];

export = slashCommands;


