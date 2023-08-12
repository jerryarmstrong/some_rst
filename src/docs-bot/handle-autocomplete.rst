src/docs-bot/handle-autocomplete.ts
===================================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import algoliasearch, { SearchIndex } from 'algoliasearch';
import { ApplicationCommandOptionChoice, AutocompleteInteraction, Interaction } from 'discord.js';
import dotenv from 'dotenv';
dotenv.config();

const ALGOLIA_APP_METAPLEX = process.env.ALGOLIA_APP_METAPLEX ?? 'MISSING';
const ALGOLIA_KEY_METAPLEX = process.env.ALGOLIA_KEY_METAPLEX ?? 'MISSING';
const ALGOLIA_APP_SOLANA = process.env.ALGOLIA_APP_SOLANA ?? 'MISSING';
const ALGOLIA_KEY_SOLANA = process.env.ALGOLIA_KEY_SOLANA ?? 'MISSING';

const metaplexClient = algoliasearch(ALGOLIA_APP_METAPLEX, ALGOLIA_KEY_METAPLEX);
const solanaClient = algoliasearch(ALGOLIA_APP_SOLANA, ALGOLIA_KEY_SOLANA);

export const metaplexIndex = metaplexClient.initIndex('metaplex');
export const solanaIndex = solanaClient.initIndex('solana');

type AlgoliaResults = {
    responses: string[];
    lvl0s: string[];
    links: string[];
    combined: string[];
};

type LastUserOption = {
    isSame: boolean;
    link: string;
    index: number;
    results?: AlgoliaResults;
};

const COMMAND_TO_INDEX_MAP: any = {
    docs: metaplexIndex,
    soldocs: solanaIndex,
};

const lastUserOptions = new Map<string, AlgoliaResults>();

export async function handleAutoComplete(interaction: AutocompleteInteraction) {
    const commandName = interaction.commandName;
    const user = interaction.user;
    if (lastUserOptions.size > 100) {
        for (const key in lastUserOptions.keys()) {
            if (lastUserOptions.size <= 30) break;
            lastUserOptions.delete(key);
        }
    }
    if (Object.prototype.hasOwnProperty.call(COMMAND_TO_INDEX_MAP, commandName)) {
        const focusedOption = interaction.options.getFocused(true);
        if (focusedOption.name === 'query') {
            const query = focusedOption.value;
            if (typeof query === 'number') return;
            if (query === '') {
                lastUserOptions.delete(user.id);
                //     const response = await interaction.respond([]);
                //     return;
            } else if (checkLastUserOptions(query, user.id).isSame) {
                const result: ApplicationCommandOptionChoice = {
                    name: query,
                    value: query,
                };
                const response = await interaction.respond([result]);
                return;
            }
            const algoliaResponse = await getAlgoliaResponse(
                query,
                COMMAND_TO_INDEX_MAP[commandName]
            );
            lastUserOptions.set(user.id, algoliaResponse);
            const newResponses: ApplicationCommandOptionChoice[] = algoliaResponse.combined.map(
                (choice) => {
                    const result: ApplicationCommandOptionChoice = {
                        name: choice,
                        value: choice,
                    };
                    return result;
                }
            );
            const response = await interaction.respond(newResponses);
        }
    }
}

function checkLastUserOptions(query: string, userId: string): LastUserOption {
    const lastUserOption = lastUserOptions.get(userId);
    if (lastUserOption) {
        const combined = lastUserOption.combined;
        for (let i = 0; i < combined.length; i++) {
            if (query === combined[i]) {
                return {
                    isSame: true,
                    link: lastUserOption.links[i],
                    index: i,
                    results: lastUserOption,
                };
            }
        }
    }
    return { isSame: false, link: '', index: 0 };
}

export async function getAlgoliaResponse(
    query: string,
    index: any,
    hits = 10
): Promise<AlgoliaResults> {
    const result = await index.search(query, {
        attributesToRetrieve: ['type', 'hierarchy', 'url', 'hits', 'content'],
        hitsPerPage: hits,
    });
    if (!result.hits) return { responses: [], lvl0s: [], links: [], combined: [] };
    const responses: string[] = [];
    const lvl0s: string[] = [];
    const links: string[] = [];
    const combined: string[] = [];
    for (let i = 0; i < result.hits.length; i++) {
        const type: string = result.hits[i]?.type;
        let choice = '';
        let lvl0 = '';
        if (type === 'content') {
            choice = result.hits[i]?.content;
            if (!choice) return { responses: [], lvl0s: [], links: [], combined: [] };
            const length = choice.length;
            choice = choice.substring(0, Math.min(choice.length, 97));
            if (length > 97) choice = choice + '...';
        } else {
            choice = result.hits[i]?.hierarchy[type];
            lvl0 = result.hits[i]?.hierarchy['lvl0'];
        }
        if (!choice || !type) {
            continue;
        }
        links.push(result.hits[i]?.url);
        responses.push(choice);
        lvl0s.push(lvl0);
        let message = '';
        if (lvl0 === '') {
            message = choice;
        } else {
            message = `(${lvl0}) ${choice}`;
        }
        if (message.length > 100) {
            message = message.substring(0, 97) + '...';
        }
        combined.push(message);
    }
    return { responses, lvl0s, links, combined };
}

export async function algoliaResult(index: SearchIndex, interaction: Interaction) {
    if (!interaction.isCommand()) return;
    const query = interaction.options.getString('query');
    const user = interaction.options.getUser('target');
    const hidden = interaction.options.getBoolean('hidden');
    await interaction.deferReply({ ephemeral: !!hidden });
    if (typeof query !== 'string') {
        const response = await interaction.editReply('Something went wrong');
        return;
    }
    const lastOption = checkLastUserOptions(query, interaction.user.id);
    if (lastOption.isSame) {
        const first = lastOption.results?.responses[lastOption.index];
        const line2 = `**${first}**\n*${lastOption.link}*`;
        const message = (user ? `*Documentation suggestion for ${user}:*\n` : '') + line2;
        const response = await interaction.editReply(message);
        lastUserOptions.delete(interaction.user.id);
        return;
    }
    const result = await getAlgoliaResponse(query, index, 1);
    const message =
        (user ? `*Documentation suggestion for ${user}:*\n` : '') +
        `**${result.responses[0]}**\n*${result.links[0]}*`;
    const response = await interaction.editReply(message);
    lastUserOptions.delete(interaction.user.id);
}


