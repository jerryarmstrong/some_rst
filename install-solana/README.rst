install-solana/README.md
========================

Last edited: 2023-06-27 13:56:04

Contents:

.. code-block:: md

    # Install Solana

Install Solana with optional caching and verify the installed version.

```yaml
- uses: metaplex-foundation/actions/install-solana@v1
  with:
    version: stable
    cache: true
```

- Inputs:
  - `version`: The Solana version to install. Defaults to `stable`.
  - `cache`: Whether the downloaded Solana release should be cached. Defaults to `true`.


