src/types.ts
============

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { ApplicationCommandData, CommandInteraction } from 'discord.js';

export type CommandObject = {
    data: ApplicationCommandData;
    execute(interaction: CommandInteraction<'cached'> | CommandInteraction): Promise<void>;
    permissions: {
        modOnly: boolean;
    };
};


