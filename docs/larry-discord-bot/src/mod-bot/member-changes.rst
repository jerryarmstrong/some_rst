src/mod-bot/member-changes.ts
=============================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { bold } from '@discordjs/builders';
import { GuildMember } from 'discord.js';
import log from 'loglevel';
import { BOT_MASTER_ID } from '../common/constants';
import { alertEmbed, deleteReply } from '../common/messages';
import { findOrCreateModel, GuildInterface, UserRoleGroup } from './mod-mongo-model';

export const timestampToJoins = new Map<number, GuildMember[]>();
export let activeRaid = false;

export async function handleOnJoin(guildMember: GuildMember) {
    const guild = guildMember.guild;
    const model = await findOrCreateModel(guild);
    const badName = await doModCheck(guildMember, model, false);
    if (!badName) {
        if (model.verifiedRoleId && model.spamTolerance && model.logChannelId) {
            const joinedTimestamp = guildMember.joinedTimestamp;
            if (joinedTimestamp === null) throw new Error('joinedTimestamp is null...?');
            const timestamp = Math.floor(joinedTimestamp / 60000);
            const members = timestampToJoins.get(timestamp);
            if (members === undefined) {
                timestampToJoins.clear();
                timestampToJoins.set(timestamp, [guildMember]);
            } else {
                members.push(guildMember);
                if (members.length >= model.spamTolerance && !activeRaid) {
                    activeRaid = true;
                    // guild
                    //     .setVerificationLevel('HIGH', 'Raid likely')
                    //     .then(() =>
                    //         log.info(`Updated guild verification level to ${guild.verificationLevel}`)
                    //     );
                    setTimeout(async () => {
                        activeRaid = false;
                        // await guild.setVerificationLevel('MEDIUM', 'Raid timer has ended');
                        // log.info(`Updated guild verification level to ${guild.verificationLevel}`);
                    }, 1000 * 60 * 10); // 10 minute raid timer

                    const logChannel = guildMember.guild.channels.resolve(model.logChannelId);

                    if (logChannel?.isText()) {
                        logChannel.send(
                            `<@${BOT_MASTER_ID}> \n**ALERT: likely raid is happening!**`
                        );
                    }
                }
            }
        }
    }
}

export async function doModCheck(
    guildMember: GuildMember,
    model: GuildInterface,
    changeNickname = false
) {
    if (!model.isSetup) {
        const names = UserRoleGroup.fromUserRoles(model.nameCheck);
        await names.updateNameCheck(guildMember.guild, model);
    }
    if (!model.logChannelId) return;
    if (
        model.nameCheckNames?.includes(guildMember.user.username.toLowerCase()) &&
        !model.nameCheckIds?.includes(guildMember.id)
    ) {
        const dmChannel = await guildMember.createDM();
        await dmChannel.send(
            'You have an identical username to a moderator. Please change your username and rejoin.'
        );
        await guildMember.kick('User has identical username to a moderator.');
        const logChannel = guildMember.guild.channels.resolve(model.logChannelId);
        if (logChannel?.isText()) {
            const embed = alertEmbed.setDescription(
                `${bold(guildMember.user.tag)} ${bold(guildMember.id)} ${
                    changeNickname ? 'changed their nickname' : 'tried to join the server'
                } and was successfully kicked.`
            );
            logChannel.send({ embeds: [embed] });
        }
        return true;
    }
    return false;
}

export async function handleChangeUsername(guildMember: GuildMember) {
    const model = await findOrCreateModel(guildMember.guild);
    await doModCheck(guildMember, model, true);
}


