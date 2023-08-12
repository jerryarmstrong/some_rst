src/mod-bot/commands.ts
=======================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    // noinspection SpellCheckingInspection

import { CommandInteraction } from 'discord.js';
import log from 'loglevel';
import { CommandObject } from '../types';
import { handleCheckSpam, handleRemoveByJoinWindow, handleRemoveByName, handleRemoveByUser, handleRemoveSimilarJoins } from './moderation';
import {
    handleAddNameCheck,
    handleAddBotMod,
    handleLogPermissions,
    handleRemoveNameCheck,
    handleRemoveBotMod,
    handleReset,
    handleResetPermissions,
    handleSetLogChannel,
    handleSetSpamTolerance,
    handleSetVerifiedRole,
} from './change-state';

const slashCommands: CommandObject[] = [
    {
        data: {
            name: 'removeby',
            description: 'Gets rid of pesky spam/scam bots',
            defaultPermission: false,
            options: [
                {
                    name: 'user',
                    type: 1,
                    description: 'Removes multiple spam bots by user',
                    options: [
                        {
                            name: 'user',
                            description: 'One of the scam/spam bots',
                            type: 6,
                            required: true,
                        },
                        {
                            name: 'range',
                            description:
                                'Join time window to use in minutes, starting with the user',
                            type: 4,
                            required: true,
                            min_value: 1,
                            max_value: 60,
                        },
                        {
                            name: 'method',
                            description: 'kick or ban (Default: kick)',
                            type: 3,
                            required: false,
                            choices: [
                                { name: 'ban', value: 'ban' },
                                { name: 'kick', value: 'kick' },
                            ],
                        },
                        {
                            name: 'verified',
                            description: 'Include members with the verified role',
                            type: 5,
                            required: false,
                        },
                    ],
                },
                {
                    name: 'name',
                    description: 'Removes users with matching names',
                    type: 1,
                    options: [
                        {
                            name: 'name',
                            description: 'The name to check',
                            type: 3,
                            required: true,
                        },
                        {
                            name: 'type',
                            description: 'Name match type (Default: includes)',
                            type: 3,
                            required: false,
                            choices: [
                                { name: 'startswith', value: 'startswith' },
                                { name: 'endswith', value: 'endswith' },
                                { name: 'includes', value: 'includes' },
                            ],
                        },
                        {
                            name: 'method',
                            description: 'kick or ban (Default: kick)',
                            type: 3,
                            required: false,
                            choices: [
                                { name: 'ban', value: 'ban' },
                                { name: 'kick', value: 'kick' },
                            ],
                        },
                        {
                            name: 'verified',
                            description: 'Include members with the verified role',
                            type: 5,
                            required: false,
                        },
                    ],
                },
                {
                    name: 'joinwindow',
                    description: 'Remove bots that joined within a window',
                    type: 1,
                    options: [
                        {
                            name: 'first',
                            description: 'The start of the window',
                            type: 6,
                            required: true,
                        },
                        {
                            name: 'last',
                            description: 'The end of the window',
                            type: 6,
                            required: true,
                        },
                        {
                            name: 'method',
                            description: 'kick or ban (Default: kick)',
                            type: 3,
                            required: false,
                            choices: [
                                { name: 'ban', value: 'ban' },
                                { name: 'kick', value: 'kick' },
                            ],
                        },
                        {
                            name: 'verified',
                            description: 'Include members with the verified role',
                            type: 5,
                            required: false,
                        },
                    ],
                },
            ],
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            switch (interaction.options.getSubcommand(true)) {
                case 'user':
                    await handleRemoveByUser(interaction);
                    break;
                case 'name':
                    await handleRemoveByName(interaction);
                    break;
                case 'joinwindow':
                    await handleRemoveByJoinWindow(interaction);
                    break;
            }
        },
        permissions: {
            modOnly: true,
        },
    },
    {
        data: {
            name: 'set',
            description: 'Configures the settings for the guild',
            defaultPermission: false,
            options: [
                {
                    name: 'logchannel',
                    description: 'Sets the join spam log channel for the guild',
                    type: 1,
                    options: [
                        {
                            name: 'channel',
                            description: 'The channel to set',
                            type: 7,
                            required: true,
                            channel_types: [0],
                        },
                    ],
                },
                {
                    name: 'verifiedrole',
                    description: 'Sets the verified role for the guild',
                    type: 1,
                    options: [
                        {
                            name: 'role',
                            description: 'The role to set',
                            type: 8,
                            required: true,
                        },
                    ],
                },
                {
                    name: 'spamtolerance',
                    description: 'Sets the spam tolerance number for the guild',
                    type: 1,
                    options: [
                        {
                            name: 'tolerance',
                            description: 'The number of joins to be considered spam. Min: 2',
                            type: 4,
                            required: true,
                            min_value: 2,
                        },
                    ],
                },
            ],
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            switch (interaction.options.getSubcommand(true)) {
                case 'logchannel':
                    await handleSetLogChannel(interaction);
                    break;
                case 'verifiedrole':
                    await handleSetVerifiedRole(interaction);
                    break;
                case 'spamtolerance':
                    await handleSetSpamTolerance(interaction);
                    break;
            }
        },
        permissions: { modOnly: true },
    },
    {
        data: {
            name: 'namecheck',
            description: 'Adds or removes a user or a role from the name check',
            defaultPermission: false,
            options: [
                {
                    name: 'add',
                    description: 'Adds a user or a role to the name check',
                    type: 1,
                    options: [
                        {
                            name: 'user',
                            description: 'The user to add',
                            type: 6,
                            required: false,
                        },
                        {
                            name: 'role',
                            description: 'The role to add',
                            type: 8,
                            required: false,
                        },
                    ],
                },
                {
                    name: 'remove',
                    description: 'Removes a user or a role from the name check',
                    type: 1,
                    options: [
                        {
                            name: 'user',
                            description: 'The user to remove',
                            type: 6,
                            required: false,
                        },
                        {
                            name: 'role',
                            description: 'The role to remove',
                            type: 8,
                            required: false,
                        },
                    ],
                },
            ],
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            switch (interaction.options.getSubcommand(true)) {
                case 'add':
                    await handleAddNameCheck(interaction);
                    break;
                case 'remove':
                    await handleRemoveNameCheck(interaction);
                    break;
            }
        },
        permissions: { modOnly: true },
    },
    {
        data: {
            name: 'botmod',
            description: 'Adds or removes a user or a role from the bot moderator set',
            defaultPermission: false,
            options: [
                {
                    name: 'add',
                    description: 'Adds a user or a role to the bot moderator set',
                    type: 1,
                    options: [
                        {
                            name: 'user',
                            description: 'The user to add',
                            type: 6,
                            required: false,
                        },
                        {
                            name: 'role',
                            description: 'The role to add',
                            type: 8,
                            required: false,
                        },
                    ],
                },
                {
                    name: 'remove',
                    description: 'Removes a user or a role from the bot moderator set',
                    type: 1,
                    options: [
                        {
                            name: 'user',
                            description: 'The user to remove',
                            type: 6,
                            required: false,
                        },
                        {
                            name: 'role',
                            description: 'The role to remove',
                            type: 8,
                            required: false,
                        },
                    ],
                },
            ],
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            switch (interaction.options.getSubcommand(true)) {
                case 'add':
                    await handleAddBotMod(interaction);
                    break;
                case 'remove':
                    await handleRemoveBotMod(interaction);
                    break;
            }
        },
        permissions: { modOnly: true },
    },
    {
        data: {
            name: 'permissions',
            description: 'Manage botmod and namecheck permissions',
            defaultPermission: false,
            options: [
                {
                    name: 'log',
                    description: 'Logs the current mod and namecheck permissions',
                    type: 1,
                },
                {
                    name: 'reset',
                    description: 'Resets the mod and namecheck permissions for the guild',
                    type: 1,
                },
            ],
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            switch (interaction.options.getSubcommand(true)) {
                case 'log':
                    await handleLogPermissions(interaction);
                    break;
                case 'reset':
                    await handleResetPermissions(interaction);
                    break;
            }
        },
        permissions: { modOnly: true },
    },
    {
        data: {
            type: 2,
            name: 'Kick Similar Joins',
            defaultPermission: false,
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            await handleRemoveSimilarJoins(interaction, 'kick');
        },
        permissions: {
            modOnly: true,
        },
    },
    {
        data: {
            type: 2,
            name: 'Ban Similar Joins',
            defaultPermission: false,
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            await handleRemoveSimilarJoins(interaction, 'ban');
        },
        permissions: {
            modOnly: true,
        },
    },
    {
        data: {
            name: 'checkspam',
            description: 'Bot spam? Not for long',
            defaultPermission: false,
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            await handleCheckSpam(interaction);
        },
        permissions: { modOnly: true },
    },
    {
        data: {
            name: 'reset',
            description: 'Resets the state for the guild',
            defaultPermission: false,
        },
        async execute(interaction: CommandInteraction<'cached'>) {
            await handleReset(interaction);
        },
        permissions: { modOnly: true },
    },
];
export = slashCommands;


