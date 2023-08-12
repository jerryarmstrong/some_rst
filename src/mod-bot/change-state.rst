src/mod-bot/change-state.ts
===========================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { CommandInteraction, MessageEmbed } from 'discord.js';
import { resetCommandPermissions } from '../common/slash-commands';
import {
    updateMods,
    updateNameCheck,
    resetMongoPermissions,
    resetMongoModel,
    setMongoLogChannel,
    setMongoVerifiedRole,
    setMongoSpamTolerance,
    UserRoleGroup,
    findOrCreateModel,
} from './mod-mongo-model';

import { bold, channelMention, roleMention } from '@discordjs/builders';
import { deleteReply, errorEmbed, pendingEmbed, successEmbed } from '../common/messages';
import { EPHEMERAL } from '../common/constants';

export async function handleAddBotMod(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const toModify = UserRoleGroup.fromInteraction(interaction);
    const mentions = bold(toModify.toMentions());
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription(`Adding ${mentions} to the bot mods...`)],
    });
    if (!(await updateMods(interaction, toModify))) {
        const embed = errorEmbed.setDescription(`${bold('Error:')} too many overrides.`);
        await interaction.editReply({ embeds: [embed] });
        return;
    }
    await interaction.editReply({
        embeds: [successEmbed.setDescription(`Successfully added ${mentions} to the bot mods.`)],
    });
    await deleteReply(interaction);
}

export async function handleRemoveBotMod(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const toModify = UserRoleGroup.fromInteraction(interaction);
    await updateMods(interaction, toModify, true);
    const embed = successEmbed.setDescription(
        `Successfully removed ${bold(toModify.toMentions())} from the bot mods.`
    );
    await interaction.editReply({ embeds: [embed] });
    await deleteReply(interaction);
}

export async function handleAddNameCheck(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const toModify = UserRoleGroup.fromInteraction(interaction);
    const mentions = bold(toModify.toMentions());
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription(`Adding ${mentions} to the name check...`)],
    });
    await updateNameCheck(interaction.guild, toModify);
    const embed = successEmbed.setDescription(
        `Successfully added ${bold(toModify.toMentions())} to the name check.`
    );
    await interaction.editReply({ embeds: [embed] });
    await deleteReply(interaction);
}

export async function handleRemoveNameCheck(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const toModify = UserRoleGroup.fromInteraction(interaction);
    const mentions = bold(toModify.toMentions());
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription(`Removing ${mentions} from the name check...`)],
    });
    await updateNameCheck(interaction.guild, toModify, true);
    const embed = successEmbed.setDescription(
        `Successfully removed ${bold(toModify.toMentions())} from the name check.`
    );
    await interaction.editReply({ embeds: [embed] });
    await deleteReply(interaction);
}

export async function handleLogPermissions(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guild = interaction.guild;
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription('Fetching guild commands...')],
    });
    const commands = await guild.commands.fetch();
    const command = commands.find((command) => command.name === 'removeby');
    if (command === undefined) throw new Error('Command not found');
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription('Fetching guild command permissions...')],
    });
    const commandPermissions = await command.permissions.fetch({ guild: guild.id });
    const commandMentions = UserRoleGroup.fromPermissions(commandPermissions).toMentions();

    const botMods = (await findOrCreateModel(guild)).moderators;
    const botMentions = UserRoleGroup.fromUserRoles(botMods).toMentions();

    const embed = successEmbed.setDescription(
        `Current command permissions: ${bold(commandMentions)}.\n\nCurrent bot mods: ${bold(
            botMentions
        )}.`
    );
    await interaction.editReply({ embeds: [embed] });
    await deleteReply(interaction);
}

export async function handleResetPermissions(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guild = interaction.guild;
    await resetMongoPermissions(guild);
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription('Resetting command permissions...')],
    });
    await resetCommandPermissions(guild);
    await interaction.editReply({
        embeds: [successEmbed.setDescription('Successfully reset permissions.')],
    });
    await deleteReply(interaction);
}

export async function handleReset(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guild = interaction.guild;
    await resetMongoModel(guild);
    await interaction.editReply({
        embeds: [pendingEmbed.setDescription('Resetting command permissions...')],
    });
    await resetCommandPermissions(guild);
    await interaction.editReply({
        embeds: [successEmbed.setDescription('Successfully reset guild state.')],
    });
    await deleteReply(interaction);
}

export async function handleSetLogChannel(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guild = interaction.guild;
    const logChannel = interaction.options.getChannel('channel', true);
    await setMongoLogChannel(guild, logChannel.id);
    const successEmbed = new MessageEmbed()
        .setColor('GREEN')
        .setDescription(`Successfully set log channel to ${bold(channelMention(logChannel.id))}.`);
    await interaction.editReply({ embeds: [successEmbed] });
    await deleteReply(interaction);
}

export async function handleSetVerifiedRole(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guild = interaction.guild;
    const verifiedRole = interaction.options.getRole('role', true);
    await setMongoVerifiedRole(guild, verifiedRole.id);
    const embed = successEmbed.setDescription(
        `Successfully set verified role to ${bold(roleMention(verifiedRole.id))}.`
    );
    await interaction.editReply({ embeds: [embed] });
    await deleteReply(interaction);
}

export async function handleSetSpamTolerance(interaction: CommandInteraction<'cached'>) {
    await interaction.deferReply({ ephemeral: EPHEMERAL });
    const guild = interaction.guild;
    const tolerance = interaction.options.getInteger('tolerance', true);
    await setMongoSpamTolerance(guild, tolerance);
    const embed = successEmbed.setDescription(
        `Successfully set spam tolerance to ${bold(tolerance.toString())}.`
    );
    await interaction.editReply({ embeds: [embed] });
    await deleteReply(interaction);
}


