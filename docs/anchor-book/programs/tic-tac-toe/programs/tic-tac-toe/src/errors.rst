programs/tic-tac-toe/programs/tic-tac-toe/src/errors.rs
=======================================================

Last edited: 2023-07-19 14:29:33

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


