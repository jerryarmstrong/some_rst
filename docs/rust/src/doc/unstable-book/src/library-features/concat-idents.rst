src/doc/unstable-book/src/library-features/concat-idents.md
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `concat_idents`

The tracking issue for this feature is: [#29599]

[#29599]: https://github.com/rust-lang/rust/issues/29599

------------------------

The `concat_idents` feature adds a macro for concatenating multiple identifiers
into one identifier.

## Examples

```rust
#![feature(concat_idents)]

fn main() {
    fn foobar() -> u32 { 23 }
    let f = concat_idents!(foo, bar);
    assert_eq!(f(), 23);
}
```


