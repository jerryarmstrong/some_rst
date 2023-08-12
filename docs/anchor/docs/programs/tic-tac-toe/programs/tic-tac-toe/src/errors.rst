docs/programs/tic-tac-toe/programs/tic-tac-toe/src/errors.rs
============================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::error_code;

#[error_code]
pub enum TicTacToeError {
    TileOutOfBounds,
    TileAlreadySet,
    GameAlreadyOver,
    NotPlayersTurn,
    GameAlreadyStarted,
}


