src/mod-bot/moderation.ts
=========================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import {
    Collection,
    CommandInteraction,
    GuildMember,
    HTTPAttachmentData,
    MessagePayload,
} from 'discord.js';
import log from 'loglevel';
import { findOrCreateModel } from './mod-mongo-model';
import { filledBar } from 'string-progressbar';
import {
    cancelEmbed,
    countingEmbed,
    deleteReply,
    doConfirmation,
    errorEmbed,
    pendingEmbed,
    successEmbed,
} from '../common/messages';
import { bold, inlineCode, time } from '@discordjs/builders';
import { EPHEMERAL } from '../common/constants';

type NeededInfo = {
    tag: string;
    id: string;
    createTimestamp: number;
};

interface InfoObject {
    [propName: number]: NeededInfo[];
}

export async function handleCheckSpam(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    await interaction.editReply({ embeds: [countingEmbed] });
    const guild = interaction.guild;
    const guildMembers = await guild.members.fetch();
    const model = await findOrCreateModel(guild);
    const verifiedRoleId = model.verifiedRoleId ?? null;
    const spamTolerance = model.spamTolerance ?? 3;
    const embed = pendingEmbed.setDescription(
        `Found ${bold(guildMembers.size.toString())} total members. \nGetting potential bots...`
    );
    await interaction.editReply({ embeds: [embed] });
    const { infoObj, totalSus } = getQuestionableMembers(
        guildMembers,
        verifiedRoleId,
        spamTolerance
    );
    const file = await makeResultsFile(infoObj);
    await interaction.editReply({
        embeds: [successEmbed.setDescription(`Found ${bold(totalSus.toString())} potential bots.`)],
        files: [file],
    });
    await deleteReply(interaction);
}

function getQuestionableMembers(
    guildMembers: Collection<string, GuildMember>,
    verifiedRoleId: string | null,
    joinNumber: number
) {
    const joinMap = new Map<number, GuildMember[]>();
    const resultsMap = new Map<number, NeededInfo[]>();
    let totalSus = 0;
    for (const member of guildMembers.values()) {
        if (verifiedRoleId !== null) {
            if (member.roles.cache.hasAny(...[verifiedRoleId])) {
                continue;
            }
        }
        const timestamp = Math.floor((member.joinedTimestamp ?? 0) / 60000);
        const entry = joinMap.get(timestamp);
        if (entry === undefined) {
            joinMap.set(timestamp, [member]);
        } else {
            entry.push(member);
        }
    }
    for (const [key, value] of joinMap) {
        if (value.length > joinNumber) {
            totalSus += value.length;
            const neededInfo: NeededInfo[] = value.map((member) => {
                const toReturn: NeededInfo = {
                    tag: member.user.tag,
                    id: member.id,
                    createTimestamp: Math.floor(member.user.createdTimestamp / 10000000),
                };
                return toReturn;
            });
            resultsMap.set(key, neededInfo);
        }
    }
    log.info('TotalSus: ', totalSus);
    const infoObj: InfoObject = Object.fromEntries(resultsMap);
    return { infoObj: infoObj, totalSus: totalSus };
}

async function makeResultsFile(infoObj: InfoObject): Promise<HTTPAttachmentData> {
    const attachment: Buffer = Buffer.from(JSON.stringify(infoObj));
    const file = await MessagePayload.resolveFile(attachment);
    file.name = 'info.json';
    return file;
}

type MatchType = 'startswith' | 'includes' | 'endswith' | null;

type Method = 'kick' | 'ban' | null;

export async function handleRemoveByName(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const name: string = interaction.options.getString('name', true);
    const matchType = interaction.options.getString('type') as MatchType;
    const method = interaction.options.getString('method') as Method;
    const verified = interaction.options.getBoolean('verified');
    const guild = interaction.guild;

    if (name.length <= 3) {
        const embed = errorEmbed.setDescription(
            bold('Error:') + ` Name must be more than 3 characters. Please try again.`
        );
        await interaction.editReply({ embeds: [embed] });
        return;
    }
    await interaction.editReply({ embeds: [countingEmbed] });

    const model = await findOrCreateModel(guild);
    const verifiedRoleId = model.verifiedRoleId ?? null;

    if (verifiedRoleId === null && !verified) {
        const embed = errorEmbed.setDescription(
            bold('Error:') +
            ` Verified role not set. Please ${inlineCode('/set verifiedrole')} and try again.`
        );
        await interaction.editReply({ embeds: [embed] });
        return;
    }
    const guildMembers = await guild.members.fetch();
    const matchingFunction =
        matchType === 'startswith'
            ? (u: string) => u.startsWith(name)
            : matchType === 'endswith'
                ? (u: string) => u.endsWith(name)
                : (u: string) => u.includes(name);
    const matchedMembers: GuildMember[] = [];
    for (const [id, member] of guildMembers) {
        if (matchingFunction(member.user.username)) {
            if (member.roles.resolve(verifiedRoleId ?? '') == null) matchedMembers.push(member);
        }
    }
    await checkAndRemove(matchedMembers, interaction, method);
    await deleteReply(interaction);
}

export async function handleRemoveByUser(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const user = interaction.options.getUser('user', true);
    const range = interaction.options.getInteger('range', true);
    const method = interaction.options.getString('method') as Method;
    const verified = interaction.options.getBoolean('verified');
    await interaction.editReply({ embeds: [countingEmbed] });

    const guild = interaction.guild;
    const model = await findOrCreateModel(guild);
    const verifiedRoleId = model.verifiedRoleId ?? null;
    if (verifiedRoleId === null && !verified) {
        const embed = errorEmbed.setDescription(
            bold('Error:') +
            ` Verified role not set. Please ${inlineCode('/set verifiedrole')} and try again.`
        );
        await interaction.editReply({ embeds: [embed] });
        return;
    }

    const joinedTimestamp = guild.members.resolve(user)?.joinedTimestamp;
    if (joinedTimestamp === null || joinedTimestamp === undefined) return;
    const startTime = Math.floor(joinedTimestamp / 60000);
    const endTime = startTime + range;

    const guildMembers = await guild.members.fetch();
    const matchedMembers: GuildMember[] = [];
    for (const [id, member] of guildMembers) {
        const joinTimestamp = member.joinedTimestamp;
        if (joinTimestamp !== null) {
            const joinTime = Math.floor(joinTimestamp / 60000);
            if (startTime <= joinTime && joinTime <= endTime) {
                if (member.roles.resolve(verifiedRoleId ?? '') == null) matchedMembers.push(member);
            }
        }
    }
    await checkAndRemove(matchedMembers, interaction, method);
    await deleteReply(interaction);
}

export async function handleRemoveByJoinWindow(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const first = interaction.options.getUser('first', true);
    const last = interaction.options.getUser('last', true);
    const method = interaction.options.getString('method') as Method;
    const verified = interaction.options.getBoolean('verified');
    await interaction.editReply({ embeds: [countingEmbed] });

    const guild = interaction.guild;
    const model = await findOrCreateModel(guild);
    const verifiedRoleId = model.verifiedRoleId ?? null;
    if (verifiedRoleId === null && !verified) {
        const embed = errorEmbed.setDescription(
            bold('Error:') +
            ` Verified role not set. Please ${inlineCode('/set verifiedrole')} and try again.`
        );
        await interaction.editReply({ embeds: [embed] });
        return;
    }
    const startTimestamp = guild.members.resolve(first)?.joinedTimestamp;
    if (startTimestamp === null || startTimestamp === undefined) return;
    const startTime = Math.floor(startTimestamp / 60000);
    const endTimestamp = guild.members.resolve(last)?.joinedTimestamp;
    if (endTimestamp === null || endTimestamp === undefined) return;
    const endTime = Math.floor(endTimestamp / 60000);
    const guildMembers = await guild.members.fetch();
    const matchedMembers: GuildMember[] = [];
    for (const [id, member] of guildMembers) {
        const joinTimestamp = member.joinedTimestamp;
        if (joinTimestamp !== null) {
            const joinTime = Math.floor(joinTimestamp / 60000);
            if (startTime <= joinTime && joinTime <= endTime) {
                if (member.roles.resolve(verifiedRoleId ?? '') == null) matchedMembers.push(member);
            }
        }
    }
    await checkAndRemove(matchedMembers, interaction, method);
    await deleteReply(interaction);
}

export async function handleRemoveSimilarJoins(interaction: CommandInteraction<'cached'>, method: Method) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guildMember = interaction.member;
    await interaction.editReply({ embeds: [countingEmbed] });
    const guild = interaction.guild;
    const model = await findOrCreateModel(guild);
    const verifiedRoleId = model.verifiedRoleId ?? null;
    if (verifiedRoleId === null) {
        const embed = errorEmbed.setDescription(
            bold('Error:') +
            ` Verified role not set. Please ${inlineCode('/set verifiedrole')} and try again.`
        );
        await interaction.editReply({ embeds: [embed] });
        return;
    }
    const joinedTimestamp = guildMember.joinedTimestamp;
    if (joinedTimestamp === null) return;
    const startTime = Math.floor(joinedTimestamp / 60000);
    const endTime = startTime + 2;

    const guildMembers = await guild.members.fetch();
    const matchedMembers: GuildMember[] = [];
    for (const [id, member] of guildMembers) {
        const joinTimestamp = member.joinedTimestamp;
        if (joinTimestamp !== null) {
            const joinTime = Math.floor(joinTimestamp / 60000);
            if (startTime <= joinTime && joinTime <= endTime) {
                if (member.roles.resolve(verifiedRoleId ?? '') == null) matchedMembers.push(member);
            }
        }
    }
    await checkAndRemove(matchedMembers, interaction, method);
    await deleteReply(interaction);
}

export async function checkAndRemove(
    matchedMembers: GuildMember[],
    interaction: CommandInteraction<'cached'>,
    method: Method
) {
    const confirmed = await doConfirmation(
        interaction,
        `Are you sure you want to ${method ?? 'kick'} ${bold(
            matchedMembers.length.toString()
        )} members?`
    );
    console.log('Confirmed: ', confirmed);
    const length = matchedMembers.length;
    if (confirmed) {
        if (method === 'ban') {
            const embed = pendingEmbed.setDescription(
                `Banning ${bold(length.toString())} ${length === 1 ? 'member' : 'members'}...`
            );
            await interaction.editReply({ components: [], embeds: [embed] });
        } else {
            const embed = pendingEmbed.setDescription(
                `Kicking ${bold(length.toString())} ${length === 1 ? 'member' : 'members'}...`
            );
            await interaction.editReply({ components: [], embeds: [embed] });
        }
    } else {
        await interaction.editReply({ components: [], embeds: [cancelEmbed] });
    }
}

async function banMembers(list: GuildMember[], interaction: CommandInteraction<'cached'>) {
    const guild = interaction.guild;
    // const banPromises = list.map(member => guild.bans.create(member));
}

async function kickMembers(list: GuildMember[], interaction: CommandInteraction<'cached'>) {
    const guild = interaction.guild;
}


