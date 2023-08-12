src/mod-bot/mod-mongo-model.ts
==============================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { roleMention, userMention } from '@discordjs/builders';
import { ApplicationCommandPermissionData, CommandInteraction, Guild } from 'discord.js';
import log from 'loglevel';
import { model, Schema } from 'mongoose';
import { BOT_MASTER_ID } from '../common/constants';
import { updateCommandPermissions } from '../common/slash-commands';

export type UserRoles = {
    userIds: string[];
    roleIds: string[];
};

export type NameCheck = {
    names: string[];
    memberIds: string[];
};

export class UserRoleGroup {
    userIds: string[];
    roleIds: string[];

    constructor(userIds: string[], roleIds: string[]) {
        this.userIds = [...new Set(userIds)];
        this.roleIds = [...new Set(roleIds)];
    }

    static fromPermissions(permissions: ApplicationCommandPermissionData[]) {
        const userIds: string[] = [];
        const roleIds: string[] = [];
        for (const permission of permissions) {
            if (permission.type === 'USER') {
                userIds.push(permission.id);
            } else {
                roleIds.push(permission.id);
            }
        }
        return new UserRoleGroup(userIds, roleIds);
    }

    static fromInteraction(interaction: CommandInteraction<'cached'>) {
        const options = interaction.options;
        const userId = options.getUser('user')?.id;
        const roleId = options.getRole('role')?.id;
        return new UserRoleGroup(userId ? [userId] : [], roleId ? [roleId] : []);
    }

    static fromUserRoles(userRoles: UserRoles) {
        return new UserRoleGroup(userRoles.userIds, userRoles.roleIds);
    }

    static defaultMod(guild: Guild) {
        return new UserRoleGroup([BOT_MASTER_ID, guild.ownerId], []);
    }

    static empty() {
        return new UserRoleGroup([], []);
    }

    toPermissions() {
        const rolePermissions: ApplicationCommandPermissionData[] = [...this.roleIds].map((id) => ({
            id: id,
            type: 'ROLE',
            permission: true,
        }));
        const userPermissions: ApplicationCommandPermissionData[] = [...this.userIds].map((id) => ({
            id: id,
            type: 'USER',
            permission: true,
        }));
        return rolePermissions.concat(userPermissions);
    }

    toUserRoles(): UserRoles {
        return {
            userIds: this.userIds,
            roleIds: this.roleIds,
        };
    }

    add(group: UserRoleGroup) {
        for (const userId of group.userIds) {
            if (!this.userIds.includes(userId)) {
                this.userIds.push(userId);
            }
        }
        for (const roleId of group.roleIds) {
            if (!this.roleIds.includes(roleId)) {
                this.roleIds.push(roleId);
            }
        }
        return true;
    }

    remove(group: UserRoleGroup) {
        this.userIds = this.userIds.filter((userId) => !group.userIds.includes(userId));
        this.roleIds = this.roleIds.filter((roleId) => !group.roleIds.includes(roleId));
    }

    protectedRemove(group: UserRoleGroup, guild: Guild) {
        this.remove(group);
        if (!this.userIds.includes(BOT_MASTER_ID)) this.userIds.push(BOT_MASTER_ID);
        if (!this.userIds.includes(guild.ownerId)) this.userIds.push(guild.ownerId);
    }

    protectedAdd(group: UserRoleGroup) {
        this.add(group);
        console.log(this.size());
        return this.size() <= 10;

    }

    checkAdmin(guild: Guild) {
        this.userIds.forEach((id) => {
            const member = guild.members.resolve(id);
            if (member?.permissions.has('ADMINISTRATOR')) return true;
        });
        return false;
    }

    size() {
        return this.userIds.length + this.roleIds.length;
    }

    toMentions() {
        const mentions: string[] = this.userIds.map((id) => userMention(id));
        mentions.push(...this.roleIds.map((id) => roleMention(id)));
        return mentions.join(', ');
    }

    async updateNameCheck(guild: Guild, model: GuildInterface) {
        const names: string[] = [];
        const memberIds: string[] = [];
        const roles = this.roleIds;
        const guildMembers = await guild.members.fetch();
        guildMembers.forEach((member) => {
            if (member.roles.cache.hasAny(...roles)) {
                names.push(member.user.username.toLowerCase());
                memberIds.push(member.id);
            }
        });
        const members = this.userIds.map((id) => guild.members.resolve(id));
        for (const member of members) {
            if (member !== null) {
                names.push(member.user.username.toLowerCase());
                memberIds.push(member.id);
            }
        }
        model.nameCheckNames = names;
        model.nameCheckIds = memberIds;
        model.isSetup = true;

        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        //@ts-ignore
        model.markModified('nameCheckNames');
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        //@ts-ignore
        model.markModified('nameCheckIds');
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        //@ts-ignore
        model.markModified('isSetup');
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        //@ts-ignore
        await model.save();
    }
}
export interface GuildInterface {
    guildId: string;
    moderators: UserRoles;
    nameCheck: UserRoles;
    nameCheckNames?: string[];
    nameCheckIds?: string[];
    logChannelId?: string;
    verifiedRoleId?: string;
    spamTolerance?: number;
    isSetup?: boolean;
}

export const GuildSchema = new Schema({
    guildId: String,
    moderators: {
        roleIds: [String],
        userIds: [String],
    },
    nameCheck: {
        roleIds: [String],
        userIds: [String],
    },
    nameCheckNames: [String],
    nameCheckIds: [String],
    logChannelId: String,
    verifiedRoleId: String,
    spamTolerance: Number,
    isSetup: Boolean,
});

export async function updateMods(
    interaction: CommandInteraction<'cached'>,
    toModify: UserRoleGroup,
    remove = false
) {
    const guild = interaction.guild;
    const targetGuild = await findOrCreateModel(guild);
    const mods = UserRoleGroup.fromUserRoles(targetGuild.moderators);
    if (remove) {
        mods.protectedRemove(toModify, guild);
    } else {
        if (!mods.protectedAdd(toModify)) return false;
    }
    targetGuild.moderators = mods.toUserRoles();
    console.log('Mods: ', mods);
    targetGuild.markModified('moderators');
    await targetGuild.save();
    await updateCommandPermissions(mods, guild);
    return true;
}

export async function updateNameCheck(guild: Guild, toModify: UserRoleGroup, remove = false) {
    const targetGuild = await findOrCreateModel(guild);
    const nameCheck = UserRoleGroup.fromUserRoles(targetGuild.nameCheck);
    await nameCheck.updateNameCheck(guild, targetGuild);
    if (remove) {
        nameCheck.remove(toModify);
    } else {
        nameCheck.add(toModify);
    }
    targetGuild.markModified('nameCheck');
    await targetGuild.save();
}

export async function defaultModel(guild: Guild) {
    return GuildModel.create({
        guildId: guild.id,
        moderators: {
            roleIds: [],
            userIds: [BOT_MASTER_ID, guild.ownerId],
        },
        nameCheck: {
            roleIds: [],
            userIds: [],
        },
    });
}

export async function resetMongoModel(guild: Guild) {
    await GuildModel.deleteOne({ guildId: guild.id });
    const targetGuild = await defaultModel(guild);
    await targetGuild.save();
}

export async function resetMongoPermissions(guild: Guild) {
    const targetGuild = await findOrCreateModel(guild);
    targetGuild.moderators = {
        roleIds: [],
        userIds: [BOT_MASTER_ID, guild.ownerId],
    };
    targetGuild.markModified('moderators');
    await targetGuild.save();
    return targetGuild;
}

export async function findOrCreateModel(guild: Guild) {
    let targetGuild = await GuildModel.findOne({ guildId: guild.id });
    if (!targetGuild) {
        targetGuild = await defaultModel(guild);
    }
    return targetGuild;
}

export async function setMongoLogChannel(guild: Guild, channelId: string) {
    const targetGuild = await findOrCreateModel(guild);
    targetGuild.logChannelId = channelId;
    targetGuild.markModified('logChannelId');
    await targetGuild.save();
}

export async function setMongoVerifiedRole(guild: Guild, verifiedRoleId: string) {
    const targetGuild = await findOrCreateModel(guild);
    targetGuild.verifiedRoleId = verifiedRoleId;
    targetGuild.markModified('verifiedRoleId');
    await targetGuild.save();
}

export async function setMongoSpamTolerance(guild: Guild, spamTolerance: number) {
    const targetGuild = await findOrCreateModel(guild);
    targetGuild.spamTolerance = spamTolerance;
    targetGuild.markModified('spamTolerance');
    await targetGuild.save();
}

export const GuildModel = model<GuildInterface>('guildschema', GuildSchema);


