src/docs-bot/wtf-is.ts
======================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { CommandInteraction } from 'discord.js';
import * as child_process from 'child_process';
import * as util from 'util';

export async function wtfIs(interaction: CommandInteraction) {
    const query = interaction.options.getString('code', true);
    const hidden = interaction.options.getBoolean('hidden');

    await interaction.deferReply({ ephemeral: hidden ?? true });

    let response;
    try {
        // Uses the `metaboss` crate made by Sam Vanderwaal.
        // https://crates.io/crates/metaboss
        const execFile = util.promisify(child_process.execFile);
        const stdout = await (await execFile('metaboss', ['find','error',query])).stdout;
        response = stdout.replace('Done!','')
    } catch (e) {
        response = `Error: Invalid Error Code ${query}`;
    }
    const message = `**Response from *metaboss find error*:**\n${response}`;
    await interaction.editReply(message);
}

