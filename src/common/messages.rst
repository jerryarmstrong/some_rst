src/common/messages.ts
======================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import {
    ButtonInteraction,
    CommandInteraction,
    MessageActionRow,
    MessageButton,
    MessageEmbed,
} from 'discord.js';

const confirmButton = new MessageButton()
    .setCustomId('confirm')
    .setLabel('Confirm')
    .setStyle('SUCCESS');

const cancelButton = new MessageButton()
    .setCustomId('cancel')
    .setLabel('Cancel')
    .setStyle('DANGER');

export const errorEmbed = new MessageEmbed().setColor('RED');
export const successEmbed = new MessageEmbed().setColor('GREEN');
export const pendingEmbed = new MessageEmbed().setColor('ORANGE');
export const alertEmbed = new MessageEmbed().setColor('YELLOW');

export const countingEmbed = new MessageEmbed()
    .setDescription('Counting members. Please wait...')
    .setColor('ORANGE');

export const cancelEmbed = new MessageEmbed()
    .setDescription(`Interaction cancelled.`)
    .setColor('RED');

export async function doConfirmation(interaction: CommandInteraction<'cached'>, message: string) {
    const embed = pendingEmbed.setDescription(message);
    const row = new MessageActionRow().addComponents(confirmButton, cancelButton);
    await interaction.editReply({ embeds: [embed], components: [row] });
    const lastMessage = await interaction.fetchReply();

    const filter = (i: ButtonInteraction<'cached'>) => {
        i.deferUpdate();
        return i.user.id === interaction.user.id;
    };
    const click = await lastMessage.awaitMessageComponent({
        filter,
        componentType: 'BUTTON',
        time: 15000,
    }).catch(() => false);
    if (typeof click === 'boolean') return false;
    return click.customId === 'confirm';
}

export async function deleteReply(interaction: CommandInteraction<'cached'>) {
    if (!interaction.ephemeral) {
        setTimeout(async () => {
            await interaction.deleteReply();
        }, 10000);
    }
}


