cache-program/README.md
=======================

Last edited: 2023-06-27 13:56:04

Contents:

.. code-block:: md

    # Cache program dependencies

Cache all folders related to the given folder. This includes Rust global folders and its `target` folder.

```yaml
- uses: metaplex-foundation/actions/cache-program@v1
  with:
    folder: ./programs/mpl-token-metadata
    key: program-token-metadata
```

- Inputs:
  - `folder`: Path to the folder containing the program (without trailing slash). **Required**.
  - `key`: A unique key prefix for the cache identifying the program. **Required**.


