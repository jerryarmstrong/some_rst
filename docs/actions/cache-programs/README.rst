cache-programs/README.md
========================

Last edited: 2023-06-27 13:56:04

Contents:

.. code-block:: md

    # Cache all programs dependencies

Cache all program related folders. This includes Rust global folders and all `target` folders under a given folder.

```yaml
- uses: metaplex-foundation/actions/cache-programs@v1
  with:
    folder: ./programs
    key: programs
```

- Inputs:
  - `folder`: Path to the folder containing the programs (without trailing slash). Defaults to `./programs`.
  - `key`: A unique key prefix for the cache. Defaults to `programs`.


