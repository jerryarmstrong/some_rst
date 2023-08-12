cache-idl-generators/README.md
==============================

Last edited: 2023-06-27 13:56:04

Contents:

.. code-block:: md

    # Cache IDL generators

Cache the hidden folder that caches IDL generators such as Shank and Anchor.

```yaml
- uses: metaplex-foundation/actions/cache-idl-generators@v1
  with:
    path: ./.crates/
    key: idl-generators
```

- Inputs:
  - `path`: Path(s) to cache. Defaults to `./.crates/`.
  - `key`: A unique key prefix for the cache. Defaults to `idl-generators`.


