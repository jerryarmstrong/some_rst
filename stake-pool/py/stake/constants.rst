stake-pool/py/stake/constants.py
================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: py

    """Stake Program Constants."""

from solana.publickey import PublicKey

STAKE_PROGRAM_ID: PublicKey = PublicKey("Stake11111111111111111111111111111111111111")
"""Public key that identifies the Stake program."""

SYSVAR_STAKE_CONFIG_ID: PublicKey = PublicKey("StakeConfig11111111111111111111111111111111")
"""Public key that identifies the Stake config sysvar."""

STAKE_LEN: int = 200
"""Size of stake account."""

LAMPORTS_PER_SOL: int = 1_000_000_000
"""Number of lamports per SOL"""

MINIMUM_DELEGATION: int = LAMPORTS_PER_SOL
"""Minimum delegation allowed by the stake program"""


