src/docs-bot.ts
===============

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { handleAutoComplete } from './docs-bot/handle-autocomplete';
import { Interaction, Client, Intents } from 'discord.js';
import { getCommands, setupCommands } from './common/slash-commands';
import docsCommands from './docs-bot/commands';
import log from 'loglevel';
import dotenv from 'dotenv';
import { EPHEMERAL } from './common/constants';
import { connectDatabase } from './common/connect-db';
dotenv.config();

log.setLevel(log.levels.INFO);

process.on('unhandledRejection', (error) => {
    log.warn('Unhandled promise rejection:', error);
});

// Create a new discord client
const client = new Client({
    intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MEMBERS],
});

// When the client is ready, run this code (only once)
client.login(process.env.DOCS_BOT_TOKEN);

client.once('ready', async () => {
    log.info('Ready!');
    // const mongoUri = process.env.MOD_BOT_MONGO_URI;
    // if (mongoUri === undefined) {
    //     throw new Error('Bad mongo env');
    // }
    // await connectDatabase(mongoUri);
    await main();
});

async function main() {
    if (!client.isReady()) return;
    // noinspection JSUnusedLocalSymbols
    const { guilds, commands } = await setupCommands(client, docsCommands, false);
    // const commands = getCommands(docsCommands);
    client.on('interactionCreate', async (interaction: Interaction) => {
        if (interaction.isAutocomplete()) {
            await handleAutoComplete(interaction);
            return;
        }

        if (!interaction.isCommand()) return;

        const command = commands.get(interaction.commandName);

        if (!command) return;
        log.debug(interaction.commandName);
        try {
            await command.execute(interaction);
        } catch (error) {
            log.warn(error);
            await interaction.reply({
                content: 'There was an error while executing this command!',
                ephemeral: EPHEMERAL,
            });
        }
    });
}


