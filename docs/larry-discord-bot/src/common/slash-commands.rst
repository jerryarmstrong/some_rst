src/common/slash-commands.ts
============================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import {
    ApplicationCommandPermissionData,
    Client,
    Collection,
    Guild,
    GuildApplicationCommandPermissionData,
    OAuth2Guild,
} from 'discord.js';
import { CommandObject } from '../types';
import log from 'loglevel';
import { defaultModel, GuildModel, UserRoleGroup } from '../mod-bot/mod-mongo-model';
import { BOT_MASTER_ID } from './constants';

export function getCommands(commandObjects: CommandObject[]) {
    const commands = new Collection<string, CommandObject>();

    for (const commandObj of commandObjects) {
        commands.set(commandObj.data.name, commandObj);
    }
    return commands;
}

export async function deleteGlobalCommands(client: Client<true>) {
    await client.application.commands.set([]);
    log.info(
        `Cleared all global commands for: ${client.application.name ?? client.application.id}`,
    );
}

export async function setGuildCommands(
    slashCommands: CommandObject[],
    guild: Guild,
    modIds: UserRoleGroup,
) {
    await guild.commands.set([]);
    log.info(`Cleared all guild commands for: ${guild.name}`);
    for (const command of slashCommands) {
        await guild.commands.create(command.data);
        log.debug(`Set ${command.data.name} command for: ${guild.name}`);
    }
    log.info(`Setting guild command permissions for: ${guild.name}`);
    await updateCommandPermissions(modIds, guild);
    log.info('Finished setting commands for: ', guild.name);
}

export async function updateCommandPermissions(ids: UserRoleGroup, guild: Guild) {
    const commands = await guild.commands.fetch();
    const permissionsArray: GuildApplicationCommandPermissionData[] = [];
    const permissions = ids.toPermissions();
    for (const [id] of commands) {
        permissionsArray.push({
            id: id,
            permissions: permissions,
        });
    }
    await guild.commands.permissions.set({
        fullPermissions: permissionsArray,
    });
}

export async function resetCommandPermissions(guild: Guild) {
    const commands = await guild.commands.fetch();
    const permissionsArray: GuildApplicationCommandPermissionData[] = [];
    const permissions: ApplicationCommandPermissionData[] = [
        {
            id: BOT_MASTER_ID,
            type: 'USER',
            permission: true,
        },
        {
            id: guild.ownerId,
            type: 'USER',
            permission: true,
        },
    ];
    for (const [id] of commands) {
        permissionsArray.push({
            id: id,
            permissions: permissions,
        });
    }
    await guild.commands.permissions.set({
        fullPermissions: permissionsArray,
    });
}

export async function setupCommands(client: Client<true>, slashCommands: CommandObject[], useDB = true) {
    // await deleteGlobalCommands(client);
    log.debug('Fetching all guilds...');
    const partialGuilds = await client.guilds.fetch();
    log.debug(`Fetched ${partialGuilds.size} partial guilds.`);
    const guilds: Guild[] = [];
    for (const [, guild] of partialGuilds) {
        try {
            const newGuild = await setupGuild(guild, slashCommands, useDB);
            guilds.push(newGuild);
        } catch (err) {
            log.error(`Failed to setup guild with name <${guild.name}> and id <${guild.id}>:`, err);
        }
    }
    const commands = getCommands(slashCommands);
    return { guilds, commands };
}

export async function setupGuild(guild: OAuth2Guild | Guild, slashCommands: CommandObject[], useDB: boolean) {
    let fetchedGuild: Guild;
    if (guild instanceof OAuth2Guild) {
        fetchedGuild = await guild.fetch();
    } else {
        fetchedGuild = guild;
    }
    log.debug(`Fetched ${fetchedGuild.name}.`);
    let targetGuild;
    if (useDB) {
        targetGuild = await GuildModel.findOne({ guildId: guild.id });
        if (!targetGuild) {
            targetGuild = await defaultModel(fetchedGuild);
        }
    }
    await setGuildCommands(
        slashCommands,
        fetchedGuild,
        targetGuild ? UserRoleGroup.fromUserRoles(targetGuild.moderators) : UserRoleGroup.defaultMod(fetchedGuild),
    );

    return fetchedGuild;
}


