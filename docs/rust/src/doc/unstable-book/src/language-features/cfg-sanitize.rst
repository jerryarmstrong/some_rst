src/doc/unstable-book/src/language-features/cfg-sanitize.md
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `cfg_sanitize`

The tracking issue for this feature is: [#39699]

[#39699]: https://github.com/rust-lang/rust/issues/39699

------------------------

The `cfg_sanitize` feature makes it possible to execute different code
depending on whether a particular sanitizer is enabled or not.

## Examples

```rust
#![feature(cfg_sanitize)]

#[cfg(sanitize = "thread")]
fn a() {
    // ...
}

#[cfg(not(sanitize = "thread"))]
fn a() {
    // ...
}

fn b() {
    if cfg!(sanitize = "leak") {
        // ...
    } else {
        // ...
    }
}
```


