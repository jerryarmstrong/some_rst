programs/tic-tac-toe/programs/tic-tac-toe/src/instructions/play.rs
==================================================================

Last edited: 2023-07-19 14:29:33

Contents:

.. code-block:: rs

    use crate::errors::TicTacToeError;
use crate::state::game::*;
use anchor_lang::prelude::*;

pub fn play(ctx: Context<Play>, tile: Tile) -> Result<()> {
    let game = &mut ctx.accounts.game;

    require_keys_eq!(
        game.current_player(),
        ctx.accounts.player.key(),
        TicTacToeError::NotPlayersTurn
    );

    game.play(&tile)
}

#[derive(Accounts)]
pub struct Play<'info> {
    #[account(mut)]
    pub game: Account<'info, Game>,
    pub player: Signer<'info>,
}


